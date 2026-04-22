# School Assistant AI | Enterprise RAG & Micro-LLM System
### Built from Scratch with FastAPI, PyTorch, and Vanilla JS

---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Tech Stack and Tools Used](#2-tech-stack-and-tools-used)
3. [Project Folder Structure](#3-project-folder-structure)
4. [Hybrid Agentic RAG Architecture](#4-hybrid-agentic-rag-architecture)
5. [Local Micro-LLM & Tokenizer](#5-local-micro-llm--tokenizer)
6. [Complete Step-by-Step Run Guide](#6-complete-step-by-step-run-guide)

---

## 1. Project Overview

This project is a high-performance **Full-Stack Web Application** acting as an enterprise-grade administrative chatbot for a school. It elegantly answers user queries regarding:
- General School Communication (timings, holidays)
- Fees and Payments (tuition, installments)
- Admissions and Enrollment (deadlines, processes)
- Policies and Rules (attendance, uniforms)

Originally a prototype, it has been transformed into a fully decoupled system with a **FastAPI backend** and a beautiful, professional **HTML/CSS/JS frontend** designed specifically for school administrators and teachers.

The system relies on a **Hybrid Agentic Retrieval-Augmented Generation (RAG)** pipeline. It retrieves facts using **Semantic Vector Search**, synthesizes answers via **Google Gemini 2.5 Flash**, and has a completely offline, custom-trained **7.2M Parameter PyTorch Micro-LLM** fallback engine.

---

## 2. Tech Stack and Tools Used

| Component | Technology Used | Purpose |
|-----------|-----------------|---------|
| **Backend API** | FastAPI, Uvicorn | High-speed async server for inference and RAG processing |
| **Frontend** | Vanilla HTML5, CSS3, JS | Responsive, premium UI with zero heavy frameworks |
| **Vector Search** | `SentenceTransformers` | `all-MiniLM-L6-v2` for semantic similarity scoring |
| **Agentic Cloud** | Google Generative AI | Uses `gemini-2.5-flash` for high-quality fact synthesis |
| **Local Fallback**| PyTorch (2.1+) | 7.2M parameter custom Transformer for offline generation |
| **Database** | JSON (`school_data.json`) | Centralized, easy-to-edit knowledge base of school facts |

---

## 3. Project Folder Structure

```
Mpr_llm/
|
+-- api.py                        Main FastAPI Backend Server (Run this!)
+-- school_data.json              Knowledge Base (Facts and Q&A)
|
+-- frontend/                     Static Web Interface
|   +-- index.html                Main Chat UI
|   +-- style.css                 Glassmorphic Design & Animations
|   +-- app.js                    Frontend logic, Chat state, API fetching
|
+-- dataset/
|   +-- dataloader.py             Implements BPE Tokenizer for PyTorch
|
+-- model/
|   +-- transformer.py            The 7.2M Parameter Transformer architecture
|
+-- checkpoints/                  Saved model weights
|   +-- micro_llm_epoch_40.pt     Best Local Weights
|
+-- requirements.txt              Python package dependencies
+-- README.md                     This documentation file
```

---

## 4. Hybrid Agentic RAG Architecture

The backend (`api.py`) utilizes an advanced multi-tier RAG logic with **Dynamic Thresholding**:

### Tier 1: Semantic Vector Retrieval (Smart Filtering)
The user's query is embedded using `all-MiniLM-L6-v2`. The system computes cosine similarity against the database (`school_data.json`). 
- **Top-K Expansion:** Retrieves up to `15` facts to ensure aggregate questions (e.g., "list all fees from class 1 to 10") do not drop data.
- **Dynamic Thresholding:** Instead of a hard cutoff, the system finds the highest-scoring fact and *only* keeps other facts that score within `0.15` points of it. This prevents the AI from regurgitating unrelated facts just because they share keywords.

### Tier 2: Agentic Cloud Synthesis (Gemini 2.5 Flash)
The retrieved facts are injected into a strict prompt sent to **Google Gemini 2.5 Flash**. The prompt strictly forbids hallucinations and forces the AI to answer *only* using the provided school facts. 

### Tier 3: Local Fallback Engine
If the API key is missing, invalid, or hits a rate limit (429), the system catches the error and instantly falls back to a **Local Engine**. If the query hits the similarity threshold, it returns the exact facts directly to the user (prefixed with "Here is the information:"). If the query is conversational, it routes to our custom **PyTorch Transformer** to generate a response locally without any internet connection.

---

## 5. Local Micro-LLM & Tokenizer

If the system is forced completely offline, it utilizes a custom-built AI model:
- **Tokenizer:** BPE (Byte Pair Encoding) via OpenAI's `tiktoken` (Vocab size: 50,257).
- **Architecture:** Decoder-Only Transformer (7.2M Parameters).
- **Hyperparameters:** `n_embd = 128`, `n_layer = 4`, `n_head = 4`.

This optimized size allows it to run smoothly on standard CPUs alongside the FastAPI server.

---

## 6. Complete Step-by-Step Run Guide

### Step 1: Install Dependencies
Ensure Python 3.10+ is installed. Open a terminal in the project directory:
```bash
pip install -r requirements.txt
```

### Step 2: Start the Backend Server
Launch the FastAPI backend using Uvicorn:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```
*Note: The server will take 10-15 seconds to load the PyTorch weights and SentenceTransformer models into memory on startup.*

### Step 3: Access the Web App
Open your web browser and go to:
```
http://localhost:8000
```

### Step 4: Demo Features
- **Cloud Mode:** The system uses a placeholder API key in the UI. Make sure a real key is loaded to experience the Gemini 2.5 Flash synthesis.
- **Offline Resilience:** If the Gemini API fails, notice how the application gracefully falls back to the local retrieval engine without crashing, ensuring stakeholders always receive an answer!
