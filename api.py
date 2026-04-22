"""
FastAPI Backend for School Assistant Micro-LLM
Replaces the Streamlit server. Exposes a /chat endpoint for the web frontend.
"""

import os
import sys
import glob
import torch
import warnings
warnings.filterwarnings("ignore")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)

from dataset.dataloader import BPETokenizer
from model.transformer import MicroLLM, MicroLLMConfig
from sentence_transformers import SentenceTransformer, util

# ─── App Setup ───────────────────────────────────────────────────────────────
app = FastAPI(title="School Assistant Micro-LLM API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Load Models Once At Startup ─────────────────────────────────────────────
import re
import json
import random

# ─── Load Knowledge Base from JSON ───────────────────────────────────────────
DATA_PATH = os.path.join(ROOT, "school_data.json")
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r") as f:
        KNOWLEDGE_BASE = json.load(f)
else:
    # Fallback if file is missing
    KNOWLEDGE_BASE = {"General": []}

qa_index = []
for category, items in KNOWLEDGE_BASE.items():
    for item in items:
        base_q = item["question"]
        ans = item["answer"]
        variations = item.get("variations", [])
        
        qa_index.append((base_q, ans))
        for v in variations:
            qa_index.append((v, ans))

tokenizer = BPETokenizer()
embedder = SentenceTransformer('all-MiniLM-L6-v2')
questions = [q for q, a in qa_index]
qa_embeddings = embedder.encode(questions, convert_to_tensor=True)

def get_epoch(f):
    m = re.search(r'epoch_(\d+)', f)
    return int(m.group(1)) if m else -1

ckpt_dir = os.path.join(ROOT, "checkpoints")
ckpts = sorted(glob.glob(os.path.join(ckpt_dir, "micro_llm_epoch_*.pt")), key=get_epoch)
ckpt_path = ckpts[-1] if ckpts else None

model = None
ckpt_info = {}
if ckpt_path:
    checkpoint = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    config = checkpoint["config"]
    model = MicroLLM(config)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    ckpt_info = {
        "epoch": checkpoint["epoch"],
        "loss": round(float(checkpoint["loss"]), 4),
        "params": sum(p.numel() for p in model.parameters()),
        "file": os.path.basename(ckpt_path)
    }
    print(f"[OK] Loaded: {ckpt_info['file']} | Params: {ckpt_info['params']:,} | Loss: {ckpt_info['loss']}")
else:
    print("[!] No checkpoint found. Local fallback disabled.")

print("[OK] Engine ready.")

# ─── Helper Functions ─────────────────────────────────────────────────────────
def retrieve_answers(question, top_k=8):
    q_emb = embedder.encode(question, convert_to_tensor=True)
    cosine_scores = util.cos_sim(q_emb, qa_embeddings)[0]
    
    # Task 3: Hybrid Search - Combine semantic score with keyword overlap
    q_words = set(re.findall(r'\w+', question.lower()))
    
    hybrid_scores = []
    for i, (q_text, _) in enumerate(qa_index):
        sem_score = cosine_scores[i].item()
        
        # Keyword overlap score (0.0 to 0.2 bonus)
        match_words = set(re.findall(r'\w+', q_text.lower()))
        overlap = len(q_words.intersection(match_words)) / max(len(q_words), 1)
        
        # Final score is weighted: 80% semantic, 20% keyword
        final_score = (sem_score * 0.8) + (overlap * 0.2)
        hybrid_scores.append(final_score)

    hybrid_scores = torch.tensor(hybrid_scores)
    top_results = torch.topk(hybrid_scores, k=min(top_k, len(hybrid_scores)))
    
    best_score = top_results.values[0].item()
    retrieved = [
        (qa_index[idx.item()][1], top_results.values[i].item())
        for i, idx in enumerate(top_results.indices)
    ]
    return retrieved, best_score


def is_multi_part_question(question):
    """Detect if user is asking for multiple things at once."""
    q = question.lower()
    multi_indicators = [
        ' and ', ' & ', 'all classes', 'list', 'all fees',
        'every class', 'each class', 'all the', 'different classes'
    ]
    return any(ind in q for ind in multi_indicators)


def deduplicate_facts(facts_with_scores):
    """Remove duplicate answers, keep the highest-scoring one."""
    seen = set()
    unique = []
    for fact, score in facts_with_scores:
        if fact not in seen:
            seen.add(fact)
            unique.append((fact, score))
    return unique


def extract_mentioned_classes(question):
    """
    Extract specific class/grade numbers from the question.
    Handles patterns like:
      - 'class 9 and 10'         → ['9', '10']
      - 'class 9, 10 and 7'      → ['9', '10', '7']
      - 'class 9 and class 10'   → ['9', '10']
      - 'class 9'                → ['9']
    """
    q = question.lower()

    # Step 1: Find all explicit "class/grade/std X" anchors
    anchors = re.findall(r'\b(?:class|grade|std|standard)\s*(\d+)\b', q)

    if not anchors:
        return []

    # Step 2: After the FIRST anchor, also grab any standalone numbers (1-12)
    # that appear connected by 'and', ',', '&', or spaces
    # e.g. "class 9 and 10" → after "9", grab "10"
    # Find position after first anchor match
    first_match = re.search(r'\b(?:class|grade|std|standard)\s*\d+\b', q)
    trailing_text = q[first_match.end():]  # everything after "class 9"

    # Grab numbers 1–12 that appear in the trailing text separated by , / and / &
    trailing_numbers = re.findall(
        r'(?:[\s,&]|and)\s*(\b(?:1[0-2]|[1-9])\b)',
        trailing_text
    )

    all_classes = list(set(anchors + trailing_numbers))
    return all_classes


def filter_facts_by_entities(facts_with_scores, class_numbers):
    """If specific classes are mentioned, keep only facts about those classes."""
    if not class_numbers:
        return facts_with_scores
    filtered = []
    for fact, score in facts_with_scores:
        for cls in class_numbers:
            if re.search(rf'\bclass\s*{cls}\b', fact, re.IGNORECASE):
                filtered.append((fact, score))
                break
    return filtered if filtered else facts_with_scores  # fallback if nothing matched


def format_multi_facts(facts_with_scores, threshold=0.38, question=""):
    """Combine multiple relevant facts into a clean numbered response."""
    # Filter to only the classes explicitly mentioned in the question
    class_numbers = extract_mentioned_classes(question)
    if class_numbers:
        facts_with_scores = filter_facts_by_entities(facts_with_scores, class_numbers)

    relevant = deduplicate_facts(
        [(f, s) for f, s in facts_with_scores if s >= threshold]
    )
    if not relevant:
        return None
    if len(relevant) == 1:
        return relevant[0][0]
    lines = ["Here is the information I found:\n"]
    for i, (fact, _) in enumerate(relevant, 1):
        lines.append(f"{i}. {fact}")
    return "\n".join(lines)


def generate_local(question, history=None):
    if history is None:
        history = []
    prompt = ""
    for msg in history[-4:]:
        role = "User:" if msg["role"] == "user" else "Assistant:"
        prompt += f"{role} {msg['content']}\n"
    prompt += f"User: {question}\nAssistant:"

    input_ids = torch.tensor(tokenizer.encode(prompt), dtype=torch.long).unsqueeze(0)

    with torch.no_grad():
        output_ids = model.generate(
            input_ids, max_new_tokens=120, temperature=0.2,
            top_k=5, end_token=tokenizer.eot_token
        )

    full_text = tokenizer.decode(output_ids[0].cpu().tolist())
    if "Assistant:" in full_text:
        response = full_text.split("Assistant:")[-1]
        if "User:" in response:
            response = response.split("User:")[0]
        response = response.strip()
    else:
        response = full_text[len(prompt):].strip()

    # Remove repetition loops
    words = response.split()
    if len(words) > 10:
        chunk = " ".join(words[:6])
        if response.count(chunk) >= 3:
            first = response.find(chunk)
            second = response.find(chunk, first + len(chunk))
            if second != -1:
                response = response[:second].strip()

    return response.strip() if response.strip() else "I found partial information but couldn't complete the answer. Please try rephrasing."


def refine_query_with_context(question, history):
    """
    If the question is short or contextual (e.g., 'And Class 11?'), 
    refine it using the last user question to make it searchable.
    """
    q = question.lower().strip()
    if not history or len(q.split()) > 4:
        return question

    # Find the last user question
    last_user_q = ""
    for msg in reversed(history):
        if msg["role"] == "user":
            last_user_q = msg["content"]
            break
    
    if not last_user_q:
        return question

    # Patterns for context-dependent queries
    context_triggers = ["and ", "what about", "how about", "also", "its", "it", "them"]
    
    # If it starts with a trigger or is just a class number
    is_contextual = any(q.startswith(tr) for tr in context_triggers) or re.match(r'^(?:class|grade|std)\s*\d+$', q)
    
    if is_contextual:
        # Simple refinement: Combine keywords from last question with current one
        # e.g., "What is the fee for Class 9?" + "And Class 11?" -> "fee Class 11"
        keywords = ["fee", "admission", "transport", "timing", "uniform", "attendance", "exam", "result"]
        found_key = next((k for k in keywords if k in last_user_q.lower()), "")
        
        if found_key:
            return f"{found_key} {question}"
    
    return question


def split_questions(text):
    """Task 4: Break a long message into separate searchable questions."""
    # Split by common question marks or markers
    parts = re.split(r'[?.!]', text)
    # Also handle 'and' if it looks like a separate clause
    final_questions = []
    for p in parts:
        p = p.strip()
        if len(p) > 5:
            final_questions.append(p)
    return final_questions if final_questions else [text]


def wrap_natural_language(answer, is_multi=False):
    """Task 5: Add friendly prefixes to make raw facts feel more conversational."""
    if not answer or "I'm sorry" in answer:
        return answer
        
    prefixes = [
        "Sure, here is the information:",
        "I found these details for you:",
        "Based on our records:",
        "Certainly, here you go:",
        "Here is what I found:"
    ]
    prefix = random.choice(prefixes)
    
    if is_multi:
        return f"{prefix}\n\n{answer}"
    return f"{prefix} {answer}"


def get_answer(question, history, gemini_api_key=None):
    # Task 4: Deep Parsing - Handle multi-sentence queries
    sub_questions = split_questions(question)
    all_combined_facts = []
    max_best_score = 0
    
    for sub_q in sub_questions:
        # Task 2: Refine each sub-query
        query_for_rag = refine_query_with_context(sub_q, history)
        facts_with_scores, best_score = retrieve_answers(query_for_rag, top_k=15)
        max_best_score = max(max_best_score, best_score)
        
        # Filter relevant facts for this sub-question
        class_numbers = extract_mentioned_classes(sub_q)
        if class_numbers:
            facts_with_scores = filter_facts_by_entities(facts_with_scores, class_numbers)
        
        # Filter relevant facts for this sub-question (Relaxed dynamic thresholding for multi-item queries)
        # Only keep facts that are >= 0.38 AND within 0.15 of the best score for this sub-query
        relevant = [f for f, s in facts_with_scores if s >= 0.38 and s >= (best_score - 0.15)]
        all_combined_facts.extend(relevant)

    # Deduplicate
    unique_facts = []
    for f in all_combined_facts:
        if f not in unique_facts:
            unique_facts.append(f)
    
    facts_only = unique_facts
    # Recalculate best_score overall
    best_score = max_best_score

    # ── Tier 2: Agentic Cloud (Gemini) ─────────────────────────────────────
    if gemini_api_key and gemini_api_key.strip():
        try:
            prompt = "You are a professional, intelligent School Assistant. "
            prompt += "Synthesize a fluent, complete answer to the user's question using the following school facts. "
            prompt += "Do NOT use greetings like 'Namaste', 'Hello', etc. Just provide the answer directly. "
            prompt += "If the user asks for multiple items (e.g. multiple classes, multiple fees), list ALL of them clearly. "
            prompt += "Format lists with numbered points. Be concise but complete.\n\n"
            prompt += "--- SCHOOL FACTS ---\n"
            for f in facts_only:
                prompt += f"- {f}\n"
            prompt += "\n--- CHAT HISTORY ---\n"
            for msg in history[-4:]:
                role = "User: " if msg["role"] == "user" else "Assistant: "
                prompt += f"{role}{msg['content']}\n"
            prompt += f"\nUser: {question}\nAssistant:"

            import google.generativeai as genai
            genai.configure(api_key=gemini_api_key.strip())
            model_gemini = genai.GenerativeModel("gemini-2.5-flash")
            response = model_gemini.generate_content(prompt)
            return response.text

        except Exception as e:
            print(f"[!] Cloud API Error: {str(e)}. Falling back to retrieval/local...")
            # Fall through to local tiers below

    # ── Tier 1: Smart Multi-Fact Retrieval (Strict Mode — No Hallucination) ──
    # When no API is available, we ONLY return facts from the knowledge base.
    
    if best_score >= 0.38:
        if len(unique_facts) > 1:
            lines = []
            for i, fact in enumerate(unique_facts, 1):
                lines.append(f"{i}. {fact}")
            combined_ans = "\n".join(lines)
            return wrap_natural_language(combined_ans, is_multi=True)
        elif len(unique_facts) == 1:
            return wrap_natural_language(unique_facts[0])

    # ── Below minimum confidence: politely decline rather than hallucinate ──
    if best_score < 0.30:
        return (
            "I'm sorry, I don't have specific information about that in my knowledge base. "
            "Please contact the school office directly or ask about fees, admissions, "
            "attendance, schedules, or policies."
        )

    # Moderate match but nothing useful found — return best available fact
    if facts_only:
        return wrap_natural_language(facts_only[0])
    
    return "I found some matching information but it wasn't clear. Could you please rephrase?"


# ─── Pydantic Models ──────────────────────────────────────────────────────────
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    question: str
    history: List[Message] = []
    gemini_api_key: Optional[str] = ""


# ─── API Endpoints ────────────────────────────────────────────────────────────
@app.get("/api/status")
def status():
    return {
        "status": "online",
        "model": ckpt_info.get("file", "none"),
        "params": ckpt_info.get("params", 0),
        "loss": ckpt_info.get("loss", 0),
        "epoch": ckpt_info.get("epoch", 0),
    }

@app.post("/api/chat")
def chat(req: ChatRequest):
    history = [{"role": m.role, "content": m.content} for m in req.history]
    answer = get_answer(req.question, history, req.gemini_api_key)
    return {"answer": answer}


# ─── Serve Frontend ───────────────────────────────────────────────────────────
frontend_dir = os.path.join(ROOT, "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
