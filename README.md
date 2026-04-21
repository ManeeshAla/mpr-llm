# Micro Language Model for Indian School Business Segments
### Built from Scratch using PyTorch | Enterprise Agentic Backend

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Tech Stack and Tools Used](#2-tech-stack-and-tools-used)
3. [Project Folder Structure](#3-project-folder-structure)
4. [Hybrid Agentic RAG Architecture](#4-hybrid-agentic-rag-architecture)
5. [Tokenizer: BPE (Byte Pair Encoding)](#5-tokenizer-bpe-byte-pair-encoding)
6. [Model Architecture: 7.2M Parameter Transformer](#6-model-architecture-72m-parameter-transformer)
7. [Complete Step-by-Step Run Guide](#7-complete-step-by-step-run-guide)

---

## 1. Project Overview

This project features a **Micro Language Model (Micro-LLM)** built entirely from scratch using **PyTorch**, paired with a **High-Performance Streamlit Chat Interface**. 

The system acts as a highly capable administrative chatbot for Indian School Business Segments, answering queries regarding:
- General School Communication (timings, holidays)
- Fees and Payments (tuition, installments)
- Admissions and Enrollment (RTE, deadlines)
- Policies and Rules (attendance, uniforms)

The underlying AI is a **7.2 Million Parameter Decoder-only Transformer** trained on a curated synthetic dataset of school rules. To ensure maximum reliability and accuracy, it features a **Hybrid Agentic Retrieval-Augmented Generation (RAG)** pipeline. This pipeline uses **Semantic Vector Search** to find facts, synthesized via the **Google Gemini 2.5 Flash Cloud API**, with a robust **Local PyTorch offline fallback engine**.

---

## 2. Tech Stack and Tools Used

| Tool | Purpose |
|------|---------|
| **PyTorch (2.1+)** | Deep Learning framework: builds and trains the local neural network |
| **Streamlit** | Powers the premium, responsive, dark-themed web chat interface |
| **SentenceTransformers** | Generates fast semantic vector embeddings (`all-MiniLM-L6-v2`) for retrieval |
| **Google Generative AI** | Connects to `gemini-2.5-flash` for high-end Agentic Cloud fact-synthesis |
| **tiktoken** | OpenAI BPE tokenizer (Vocabulary Size: 50,257) for enterprise-grade text parsing |

---

## 3. Project Folder Structure

```
Mpr_llm/
|
+-- app.py                        Main Streamlit Web Application (Run this!)
|
+-- dataset/
|   +-- data_generator.py         Creates the synthetic Q&A training data
|   +-- dataloader.py             Implements BPE Tokenizer for PyTorch
|   +-- school_business_data.jsonl  The generated training dataset
|
+-- model/
|   +-- transformer.py            The 7.2M Parameter Transformer architecture
|
+-- training/
|   +-- train.py                  The training loop (AdamW optimizer, checkpoints)
|
+-- inference/
|   +-- chat.py                   Legacy CLI chatbot interface
|
+-- checkpoints/                  Saved model weights
|   +-- micro_llm_epoch_40.pt     Best Local Weights
|
+-- requirements.txt              Python package dependencies
+-- README.md                     This documentation file
```

---

## 4. Hybrid Agentic RAG Architecture

The web app (`app.py`) orchestrates a brilliant three-tier fallback logic for generating answers:

### Tier 1: Semantic Vector Retrieval
The user's query is embedded using `SentenceTransformer('all-MiniLM-L6-v2')`. We compute the cosine similarity against all known facts in our cached `KNOWLEDGE_BASE`. If the confidence score is **>0.50**, the system bypasses AI generation entirely and instantly returns the exact, pre-approved school policy.

### Tier 2: Agentic Cloud Synthesis (Gemini 2.5 Flash)
If no perfect match is found, but relevant facts are retrieved, the facts are securely shipped to Google's **Gemini 2.5 Flash** API along with the conversation history. Gemini intelligently synthesizes a conversational, highly accurate answer based *only* on the provided context.
*(Note: The `google.generativeai` package is explicitly configured to use the `gemini-2.5-flash` model as older models like 1.5/1.0 no longer support the latest generated AI Studio keys).* 

### Tier 3: Generative Local Fallback
If the user is offline or the API key is removed from the sidebar, the system falls back to the locally trained PyTorch Transformer. It generates the response token-by-token using the weights loaded from `checkpoints/micro_llm_epoch_40.pt`.

---

## 5. Tokenizer: BPE (Byte Pair Encoding)

We upgraded from a naive character-level tokenizer to a state-of-the-art **BPE (Byte Pair Encoding)** tokenizer using OpenAI's `tiktoken` (`gpt2` encoding).
- **Vocabulary Size:** 50,257 tokens.
- **Advantage:** Words like "school" or "admission" become single tokens rather than 6-9 separate characters, vastly improving the context window efficiency and allowing the model to learn semantic groupings natively.

---

## 6. Model Architecture: 7.2M Parameter Transformer

Our local PyTorch model is a **Decoder-Only Transformer**. It implements Causal Self-Attention, GELU activations, and Layer Normalization.

### Key Hyperparameters:
- `vocab_size` = 50,257 
- `n_embd` = 128 (Embedding dimension)
- `n_layer` = 4 (Transformer blocks)
- `n_head` = 4 (Attention heads)
- `block_size` = 128 (Context window)

### Parameter Breakdown:
| Component | Parameters |
|-----------|-----------|
| Token Embedding (`wte`) | 50,257 x 128 = 6,432,896 |
| Positional Embedding (`wpe`) | 128 x 128 = 16,384 |
| 4x Transformer Blocks | ~800,000 |
| LM Head | Shared with `wte` (0) |
| **TOTAL** | **~7.2 Million** |

This optimized size allows it to be extremely lightweight while possessing significantly more capacity than the original 200k prototype.

---

## 7. Complete Step-by-Step Run Guide

### Step 1: Install Dependencies
Make sure Python 3.10+ is installed. Open a terminal in the project directory:
```bash
pip install -r requirements.txt
```

### Step 2: Launch the Web App
The entire system is integrated into a unified Streamlit dashboard:
```bash
streamlit run app.py
```

### Step 3: Chat!
The app will open in your browser (`http://localhost:8501`).

- The app natively caches the SentenceTransformer model on startup for blazing fast hot-reloads.
- A Gemini API Key is automatically pre-filled in the sidebar for Agentic Cloud mode.
- To force the app to use the **Local PyTorch Fallback Engine**, simply delete the API key from the sidebar text box and send your message!
