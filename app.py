import os
import sys
import json
import glob
import torch
import streamlit as st

# ── Path setup ───────────────────────────────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)

from dataset.dataloader import BPETokenizer
from model.transformer import MicroLLM, MicroLLMConfig
from sentence_transformers import SentenceTransformer, util
import google.generativeai as genai

# ═══════════════════════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="School Assistant — Micro LLM",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════
#  CUSTOM CSS — Premium Dark Theme
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #1a1a2e, #16213e);
    color: #e0e0e0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.04);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Chat message bubbles */
.user-bubble {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 12px 18px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0 8px 15%;
    box-shadow: 0 4px 15px rgba(102,126,234,0.3);
    font-size: 15px;
    line-height: 1.5;
}

.bot-bubble {
    background: rgba(255,255,255,0.07);
    color: #e8e8e8;
    padding: 12px 18px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px 15% 8px 0;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    font-size: 15px;
    line-height: 1.5;
}

.label-user {
    text-align: right;
    font-size: 11px;
    color: #667eea;
    margin: 2px 4px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.label-bot {
    text-align: left;
    font-size: 11px;
    color: #a78bfa;
    margin: 2px 4px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* Metric cards in sidebar */
.metric-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 10px;
    text-align: center;
}
.metric-value {
    font-size: 22px;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.metric-label {
    font-size: 11px;
    color: #888;
    margin-top: 2px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* Input box */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 12px !important;
    font-size: 15px !important;
    padding: 12px 16px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 2px rgba(102,126,234,0.3) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 10px 24px !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(102,126,234,0.4) !important;
}

/* Header */
.main-header {
    text-align: center;
    padding: 20px 0 10px 0;
}
.main-title {
    font-size: 32px;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #a78bfa, #f093fb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 4px;
}
.main-subtitle {
    font-size: 14px;
    color: #888;
    letter-spacing: 0.5px;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,0.08) !important;
}

/* Chat container */
.chat-container {
    max-height: 520px;
    overflow-y: auto;
    padding: 10px 5px;
}

/* Category chips */
.chip {
    display: inline-block;
    background: rgba(102,126,234,0.15);
    border: 1px solid rgba(102,126,234,0.3);
    color: #a78bfa;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    margin: 3px;
    cursor: pointer;
}

/* Status badge */
.status-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
}
.status-retrieval {
    background: rgba(16,185,129,0.15);
    color: #10b981;
    border: 1px solid rgba(16,185,129,0.3);
}
.status-generative {
    background: rgba(245,158,11,0.15);
    color: #f59e0b;
    border: 1px solid rgba(245,158,11,0.3);
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(102,126,234,0.4); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  BACKEND FUNCTIONS (cached for performance)
# ═══════════════════════════════════════════════════════════════

# Semantic Search replaces Jaccard Similarity

@st.cache_resource(show_spinner=False)
def load_model_and_data():
    ckpt_dir  = os.path.join(ROOT, "checkpoints")

    # ── Build Custom QA Index ────────────────────────────────
    from dataset.data_generator import KNOWLEDGE_BASE
    qa_index = []
    for category, facts in KNOWLEDGE_BASE.items():
        for base_q, ans, variations in facts:
            qa_index.append((base_q, ans))
            for v in variations:
                qa_index.append((v, ans))

    tokenizer = BPETokenizer()
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    questions = [q for q, a in qa_index]
    qa_embeddings = embedder.encode(questions, convert_to_tensor=True)

    # ── Load checkpoint ─────────────────────────────────────
    import re
    def get_epoch(f):
        m = re.search(r'epoch_(\d+)', f)
        return int(m.group(1)) if m else -1

    ckpts = sorted(glob.glob(os.path.join(ckpt_dir, "micro_llm_epoch_*.pt")), key=get_epoch)
    ckpt_path = ckpts[-1] if ckpts else None

    model, config, ckpt_info = None, None, {}
    if ckpt_path:
        checkpoint = torch.load(ckpt_path, map_location="cpu", weights_only=False)
        config     = checkpoint["config"]
        model      = MicroLLM(config)
        model.load_state_dict(checkpoint["model_state_dict"])
        model.eval()
        ckpt_info  = {
            "epoch": checkpoint["epoch"],
            "loss":  checkpoint["loss"],
            "params": sum(p.numel() for p in model.parameters()),
            "file":  os.path.basename(ckpt_path)
        }

    return model, tokenizer, qa_index, qa_embeddings, embedder, ckpt_info


def retrieve_answers(question, qa_index, qa_embeddings, embedder, top_k=5):
    q_emb = embedder.encode(question, convert_to_tensor=True)
    cosine_scores = util.cos_sim(q_emb, qa_embeddings)[0]
    
    top_results = torch.topk(cosine_scores, k=min(top_k, len(cosine_scores)))
    
    best_score = top_results.values[0].item()
    retrieved_facts = []
    
    for idx in top_results.indices:
        retrieved_facts.append(qa_index[idx.item()][1])
        
    return retrieved_facts, best_score, "retrieval"


def generate_answer(question, model, tokenizer, history=None):
    if history is None: history = []
    
    # Conversational Memory: keep last 2 exchanges
    prompt = ""
    for msg in history[-4:]:
        role = "User:" if msg["role"] == "user" else "Assistant:"
        prompt += f"{role} {msg['content']}\n"
    prompt += f"User: {question}\nAssistant:"

    input_ids = torch.tensor(
        tokenizer.encode(prompt), dtype=torch.long
    ).unsqueeze(0)

    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_new_tokens=120,
            temperature=0.2,
            top_k=5,
            end_token=tokenizer.eot_token
        )

    full_text = tokenizer.decode(output_ids[0].cpu().tolist())
    if "Assistant:" in full_text:
        response = full_text.split("Assistant:")[-1]
        if "User:" in response:
            response = response.split("User:")[0]
        response = response.strip()
    else:
        response = full_text[len(prompt):].strip()

    # ── Repetition detection: cut off if a phrase repeats 3+ times ──
    words = response.split()
    if len(words) > 10:
        chunk = " ".join(words[:6])  # first 6 words as a pattern
        if response.count(chunk) >= 3:
            # Take only up to the second occurrence
            first = response.find(chunk)
            second = response.find(chunk, first + len(chunk))
            if second != -1:
                response = response[:second].strip()

    # ── Sentence cap: return only first 2 clean sentences ──
    sentences = [s.strip() for s in response.replace("\n", " ").split(".") if s.strip()]
    if len(sentences) > 2:
        response = ". ".join(sentences[:2]) + "."

    return response if response else "I found partial information but couldn't complete the answer. Please try rephrasing."


def get_answer(question, model, tokenizer, qa_index, qa_embeddings, embedder, history, gemini_api_key=None):
    # Context substitution
    query_for_rag = question
    if len(history) >= 2 and len(question.strip().split()) <= 4:
        query_for_rag = f"{history[-2]['content']} {question}"

    # Get Top 5 Facts
    facts, best_score, mode = retrieve_answers(query_for_rag, qa_index, qa_embeddings, embedder, top_k=5)
    
    # ── AGENTIC CLOUD ENGINE (GEMINI) ──
    if gemini_api_key:
        try:
            prompt = "You are a friendly, intelligent Indian School Assistant. "
            prompt += "Synthesize a fluent answer to the user's question using ONLY the following facts about the school. "
            prompt += "If the facts contain multiple pieces of info, combine them cleanly. "
            prompt += "If the facts do not answer the question, answer it normally using your general internet knowledge.\n\n"
            prompt += "--- SCHOOL FACTS ---\n"
            for i, f in enumerate(facts):
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
            return response.text, "agentic", best_score
        except Exception as e:
            return f"Agentic Exception: {str(e)}", "error", best_score

    # ── LOCAL FALLBACK ENGINE ──
    if best_score >= 0.50:
        return facts[0], mode, best_score  # Exact match logic
        
    if model:
        return generate_answer(question, model, tokenizer, history), "generative", best_score
        
    return "Sorry, I could not find an answer and the generative model is offline.", "generative", best_score


# ═══════════════════════════════════════════════════════════════
#  MAIN APP
# ═══════════════════════════════════════════════════════════════

# ── Load everything ─────────────────────────────────────────
with st.spinner("Loading Enterprise AI (Semantic Search & BPE Tokenizer)..."):
    model, tokenizer, qa_index, qa_embeddings, embedder, ckpt_info = load_model_and_data()

# ── Session state ────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ═══════════════════════════════════════════════════════════════
#  SIDEBAR
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 10px 0 20px 0;'>
        <div style='font-size:40px;'>🏫</div>
        <div style='font-size:16px; font-weight:700; color:#a78bfa;'>Micro LLM</div>
        <div style='font-size:11px; color:#666;'>Indian School Business</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ── Response Mode Legend ─────────────────────────────────
    st.markdown("### ⚡ Response Modes")
    st.markdown("""
    <span class='status-badge status-retrieval'>● Retrieval</span>
    <div style='font-size:12px; color:#777; margin: 6px 0 12px 0;'>
    Exact match found in knowledge base → perfect answer returned directly.
    </div>
    <span class='status-badge' style='background: rgba(59,130,246,0.15); color: #3b82f6; border: 1px solid rgba(59,130,246,0.3);'>● Agentic (Cloud API)</span>
    <div style='font-size:12px; color:#777; margin: 6px 0 12px 0;'>
    Foundational LLM reads Top 5 DB facts & synthesizes a fluent answer.
    </div>
    <span class='status-badge status-generative'>● Generative Fallback</span>
    <div style='font-size:12px; color:#777; margin: 6px 0 12px 0;'>
    No match and no API key → Micro-LLM predicts text character-by-character.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ── Suggested Questions ──────────────────────────────────
    st.markdown("### 💡 Try Asking")
    suggestions = [
        "What is the fee for Class 8?",
        "Can I pay fees in installments?",
        "When do admissions open?",
        "What documents are required?",
        "Is transport available?",
        "What is the attendance rule?",
        "Who is the principal?",
        "When are final exams?",
    ]
    for s in suggestions:
        if st.button(s, key=f"sug_{s}"):
            st.session_state["pending_question"] = s
            st.rerun()

    # ── Agentic Mode Key Input ───────────────────────────────
    st.markdown("### ☁️ Agentic Brain Upgrade")
    gemini_key = st.text_input(
        "Gemini API Key", 
        type="password", 
        value="AIzaSyBBoTrIu0mt1cLFyuF7fNINiZG6zEzN9w4",
        help="Paste a Gemini API key here to bypass the local model and synthesize answers with Gemini."
    )
    
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# ═══════════════════════════════════════════════════════════════
#  MAIN AREA
# ═══════════════════════════════════════════════════════════════

# ── Header ───────────────────────────────────────────────────
st.markdown("""
<div class='main-header'>
    <div class='main-title'>🏫 School Assistant</div>
    <div class='main-subtitle'>
        Micro Language Model · Indian School Business Segment · Built with PyTorch
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Chat History ─────────────────────────────────────────────
chat_area = st.container()
with chat_area:
    if not st.session_state.messages:
        st.markdown("""
        <div style='text-align:center; padding: 40px 20px; color: #555;'>
            <div style='font-size:48px; margin-bottom:12px;'>💬</div>
            <div style='font-size:16px; font-weight:600; color:#777;'>
                Ask me anything about school fees, admissions, policies, or facilities!
            </div>
            <div style='font-size:13px; color:#555; margin-top:8px;'>
                Use the suggestions in the sidebar to get started.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"<div class='label-user'>YOU</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
            else:
                if msg.get("mode") == "retrieval":
                    mode_badge = "<span class='status-badge status-retrieval'>● Retrieval</span>"
                elif msg.get("mode") == "agentic":
                    mode_badge = "<span class='status-badge' style='background: rgba(59,130,246,0.15); color: #3b82f6; border: 1px solid rgba(59,130,246,0.3);'>● Agentic</span>"
                else:
                    mode_badge = "<span class='status-badge status-generative'>● Generative</span>"

                st.markdown(f"<div class='label-bot'>SCHOOL LLM &nbsp;{mode_badge}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("---")

# ── Handle sidebar suggestion click ──────────────────────────
if "pending_question" in st.session_state:
    question = st.session_state.pop("pending_question")
    st.session_state.messages.append({"role": "user", "content": question})
    with st.spinner("Thinking..."):
        answer, mode, score = get_answer(question, model, tokenizer, qa_index, qa_embeddings, embedder, st.session_state.messages, gemini_key)
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "mode": mode,
        "score": float(score)
    })
    st.rerun()

# ── Input Form (st.form prevents infinite rerun loop) ────────
with st.form(key="chat_form", clear_on_submit=True):
    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_input = st.text_input(
            label="Your question",
            placeholder="Ask a question about the school...",
            label_visibility="collapsed"
        )
    with col_btn:
        send = st.form_submit_button("Send →", use_container_width=True)

# ── Process only on explicit submit ──────────────────────────
if send and user_input.strip():
    question = user_input.strip()
    st.session_state.messages.append({"role": "user", "content": question})
    with st.spinner("Thinking..."):
        answer, mode, score = get_answer(question, model, tokenizer, qa_index, qa_embeddings, embedder, st.session_state.messages, gemini_key)
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "mode": mode,
        "score": float(score)
    })
    st.rerun()
