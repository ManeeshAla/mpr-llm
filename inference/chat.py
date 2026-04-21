import os
import sys
import json
import math
import torch

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from dataset.dataloader import CharTokenizer
from model.transformer import MicroLLM, MicroLLMConfig

# ─────────────────────────────────────────────────────────────
# RETRIEVAL LAYER
# Finds the best-matching known Q&A pair using character n-gram
# overlap. If similarity > threshold, returns the exact, clean
# answer instead of generating from the model.
# ─────────────────────────────────────────────────────────────

def get_ngrams(text, n=3):
    text = text.lower().strip()
    return set(text[i:i+n] for i in range(len(text) - n + 1))

def similarity(a, b, n=3):
    ga, gb = get_ngrams(a, n), get_ngrams(b, n)
    if not ga or not gb:
        return 0.0
    return len(ga & gb) / len(ga | gb)  # Jaccard similarity

def load_qa_index(data_file):
    """Load all unique Q&A pairs into memory for retrieval."""
    index = []
    seen = set()
    with open(data_file, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            record = json.loads(line)
            text = record.get("text", "")
            if text in seen:
                continue
            seen.add(text)
            if "\nAssistant:" in text:
                q_part, a_part = text.split("\nAssistant:", 1)
                q = q_part.replace("User:", "").strip()
                a = a_part.strip()
                index.append((q, a))
    return index

def retrieve_answer(question, index, threshold=0.35):
    """
    Returns the best matching answer from the index if similarity
    exceeds the threshold, otherwise returns None.
    """
    best_score = 0.0
    best_answer = None
    for q, a in index:
        score = similarity(question, q)
        if score > best_score:
            best_score = score
            best_answer = a
    if best_score >= threshold:
        return best_answer, best_score
    return None, best_score


# ─────────────────────────────────────────────────────────────
# TOKENIZER REBUILDER
# ─────────────────────────────────────────────────────────────

def build_tokenizer_from_data(data_file):
    lines = []
    with open(data_file, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            record = json.loads(line)
            lines.append(record.get("text", ""))
    raw_text = '\x00'.join(lines)
    return CharTokenizer(raw_text)


# ─────────────────────────────────────────────────────────────
# MAIN CHAT LOOP
# ─────────────────────────────────────────────────────────────

def chat():
    device = torch.device("cpu")
    ckpt_dir  = os.path.join(os.path.dirname(os.path.dirname(__file__)), "checkpoints")
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dataset", "school_business_data.jsonl")

    # ── Load checkpoint ──────────────────────────────────────
    if not os.path.exists(ckpt_dir) or not os.listdir(ckpt_dir):
        print("No checkpoint found. Please run `python training/train.py` first.")
        return

    ckpts     = sorted([f for f in os.listdir(ckpt_dir) if f.endswith(".pt")])
    ckpt_path = os.path.join(ckpt_dir, ckpts[-1])
    print(f"Loading checkpoint: {ckpt_path}")

    checkpoint = torch.load(ckpt_path, map_location=device, weights_only=False)
    config     = checkpoint['config']
    model      = MicroLLM(config)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.to(device)
    model.eval()

    # ── Load tokenizer & retrieval index ────────────────────
    tokenizer = build_tokenizer_from_data(data_file)
    qa_index  = load_qa_index(data_file)

    total_params = sum(p.numel() for p in model.parameters())
    print(f"Model loaded  : {total_params:,} parameters (~{total_params/1e3:.0f}K)")
    print(f"Q&A index     : {len(qa_index):,} unique pairs loaded for retrieval")
    print("-" * 58)
    print("  Micro LLM — Indian School Business Q&A Chatbot")
    print("  Type 'quit' or 'exit' to stop.")
    print("-" * 58 + "\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break

            # ── Step 1: Try retrieval first ──────────────────
            answer, score = retrieve_answer(user_input, qa_index, threshold=0.30)

            if answer:
                print(f"LLM: {answer}\n")
                continue

            # ── Step 2: Fall back to model generation ────────
            # Use very low temperature so the model sticks to
            # high-confidence characters it learned during training.
            prompt   = f"User: {user_input}\nAssistant:"
            input_ids = torch.tensor(
                tokenizer.encode(prompt), dtype=torch.long
            ).unsqueeze(0).to(device)

            with torch.no_grad():
                output_ids = model.generate(
                    input_ids,
                    max_new_tokens=120,
                    temperature=0.2,   # low = conservative = coherent
                    top_k=5,           # only pick from top 5 most likely chars
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

            print(f"LLM: {response}\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    chat()
