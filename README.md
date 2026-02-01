# 🧠 Clinical Literature RAG System for Rare Disease Decision Support

**Disease Focus:** Amyotrophic Lateral Sclerosis (ALS)  
**Domain:** Clinical / Biomedical Natural Language Processing  
**System Type:** Retrieval-Augmented Generation (RAG) with Safety Constraints  

---

## 📌 Problem Statement

Clinicians and researchers working on **rare diseases** such as ALS face major challenges:

- Clinical evidence is scattered across long, dense research papers
- Keyword-based search misses semantic meaning
- Large Language Models (LLMs) can hallucinate unsupported medical facts

### 🎯 Objective

Build a **retrieval-grounded ML system** that:
- Answers clinical questions **only using retrieved literature**
- Provides **explicit citations**
- Reports **confidence**
- Minimizes hallucinations through system design

> ⚠️ This is **not a chatbot**.  
> It is a **safety-aware Retrieval-Augmented Generation (RAG) system**.

---

## 🏗️ High-Level Architecture

Clinical PDFs (ALS literature)
↓
PDF → Text Conversion
↓
Cleaning & Semantic Chunking
↓
Biomedical Embeddings
↓
FAISS Vector Store
↓
Dense Retrieval (Recall)
↓
Cross-Encoder Re-Ranking (Precision)
↓
LLM Generation
↓
Answer + Citations + Confidence


---

## 📚 Data Sources

- PubMed Central Open-Access clinical reviews
- Peer-reviewed ALS literature
- Orphanet rare disease summaries

All sources are:
- Open access
- Research-grade
- Non-proprietary

---

## 🧩 Ingestion & Chunking Strategy

### Why chunking matters
Poor chunking leads to:
- Irrelevant retrieval
- Loss of clinical context
- Increased hallucinations

### Implemented approach
- **Section-aware semantic chunking**
- Chunked by clinical sections:
  - Diagnosis
  - Treatment
  - Prognosis
  - Pathophysiology
- Chunk size: **300–500 tokens**
- Overlap only **within the same section**

This preserves medical coherence and improves retrieval quality.

---

## 🔍 Embeddings & Retrieval

### Embeddings
- Domain-specific **biomedical sentence embeddings**
- Optimized for clinical terminology

### Vector Store
- **FAISS** for efficient similarity search
- Metadata stored per chunk:
  - Paper title
  - Section name
  - Publication year

### Retrieval
- Top-K dense retrieval
- Section filtering for relevance (e.g., diagnosis queries prioritize diagnostic sections)

---

## 🎯 Re-Ranking (Precision Layer)

Dense retrieval optimizes for **recall**, but not precision.

### Solution
- Apply a **cross-encoder re-ranker**
- Jointly score `(query, chunk)` pairs
- Retain **top 3–5 most relevant chunks**

> Dense retrieval gets recall; **re-ranking gets precision**.

This significantly improves factual grounding.

---

## ✍️ Generation Layer (Safety-First Design)

### Prompt Constraints
- The LLM **cannot answer without citations**
- If confidence is below a threshold, the system responds with:
  > *“Insufficient evidence found in retrieved literature.”*

### Output Format
- Bullet-point clinical summary
- Inline citations: `[Paper 1]`, `[Paper 2]`
- Confidence level: **Low / Medium / High**

⚠️ No diagnosis or medical advice language is permitted.

---

## 🛡️ Confidence & Safety Layer

### Confidence estimation is based on:
- Retrieval similarity scores
- Agreement across multiple sources
- Evidence coverage across independent papers

### Safety rules
- Literature-only phrasing
- No prescriptive medical advice
- Explicit uncertainty handling

---

## 📊 Evaluation Strategy

### Retrieval Evaluation
- Recall@K
- Mean Reciprocal Rank (MRR)

### Generation Evaluation
- Factual consistency with retrieved chunks
- Citation correctness
- Manual clinical sanity checks

> Accuracy alone is insufficient; **grounding and faithfulness matter more**.

---

## 🔧 Tech Stack

| Layer | Technology |
|-----|-----------|
| Ingestion | Python |
| Embeddings | HuggingFace |
| Vector Database | FAISS |
| Re-Ranking | Cross-Encoder |
| LLM | Instruction-tuned open-source model |
| API | FastAPI (planned) |
| Storage | Local |

---

## ⚠️ Failure Modes & Mitigations

| Failure Mode | Mitigation |
|-------------|-----------|
| Hallucination | Strict retrieval grounding |
| Poor recall | Semantic chunking + domain embeddings |
| Overconfidence | Confidence gating |
| Outdated info | Metadata filtering |

---

## 🧠 Why This Project Matters

This project demonstrates:
- End-to-end ML system design
- NLP and embedding-based retrieval
- Responsible LLM usage
- Clinical safety awareness
- Evaluation maturity

Designed as a **real-world applied ML system**, not a toy demo.

---

## ⚠️ Disclaimer

This system is intended for **research and educational purposes only**.  
It does **not** provide medical advice, diagnosis, or treatment recommendations.

---

## 🚀 Future Improvements

- FastAPI inference endpoint
- Interactive clinician-facing UI
- Automated citation verification
- Temporal filtering of literature

