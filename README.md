🧠 Clinical Literature RAG System for Rare Disease Decision Support

Disease focus: Amyotrophic Lateral Sclerosis (ALS)
Domain: Clinical / Biomedical NLP
Goal: Retrieval-grounded question answering over medical literature with safety constraints

📌 Problem Statement

Clinicians and researchers working on rare diseases such as ALS face major challenges:

Relevant evidence is scattered across long clinical papers

Keyword search misses semantic meaning

Large Language Models (LLMs) can hallucinate clinical facts

🎯 Objective

Build a Retrieval-Augmented Generation (RAG) system that:

Answers clinical questions only using retrieved literature

Provides citations

Reports confidence

Avoids unsafe medical claims

⚠️ This is not a chatbot — it is a retrieval-grounded ML system with explicit safety controls.

🏗️ System Architecture (High-Level)
Medical PDFs (ALS literature)
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
LLM Generation (Citation-grounded)
        ↓
Answer + Citations + Confidence

📚 Data Sources

PubMed Central Open-Access Articles

Peer-reviewed ALS clinical reviews

Orphanet rare disease summaries

All data is:

Open access

Research-grade

Non-proprietary

🧩 Ingestion & Chunking Strategy (Key Design Choice)
Why chunking matters

Poor chunking leads to:

Irrelevant retrieval

Hallucinated answers

Loss of clinical context

Implemented approach

Section-aware semantic chunking

Chunked by clinical sections:

Diagnosis

Treatment

Prognosis

Pathophysiology

300–500 tokens per chunk

Overlap only within the same section

📌 This preserves medical coherence and improves retrieval accuracy.

🔍 Embeddings & Retrieval
Embeddings

Domain-specific biomedical sentence embeddings

Optimized for clinical language and terminology

Vector Store

FAISS for efficient similarity search

Metadata stored per chunk:

Paper title

Section name

Publication year

Retrieval

Dense Top-K retrieval

Section filtering (e.g., prioritize Diagnosis for diagnostic queries)

🎯 Re-Ranking (Advanced Precision Layer)

Dense retrieval maximizes recall, but not precision.

Solution

Apply a cross-encoder re-ranker

Score (query, chunk) pairs jointly

Keep top 3–5 most relevant chunks

Dense retrieval gets recall; re-ranking gets precision.

This significantly improves answer faithfulness.

✍️ Generation Layer (Safety-First)
Prompt Constraints

The LLM cannot answer without citations

If evidence is weak → respond with:

“Insufficient evidence found in retrieved literature.”

Output Format

Bullet-point clinical summary

Inline citations: [Paper 1], [Paper 2]

Confidence level: Low / Medium / High

⚠️ No diagnosis or medical advice language is allowed.

🛡️ Confidence & Safety Layer
Confidence Score is based on:

Retrieval similarity scores

Agreement across multiple papers

Coverage across independent sources

Safety Rules

Literature-only phrasing

No prescriptive or diagnostic claims

Explicit uncertainty when evidence is limited

📊 Evaluation Strategy
Retrieval Evaluation

Recall@K

Mean Reciprocal Rank (MRR)

Generation Evaluation

Factual consistency with retrieved text

Citation correctness

Manual clinical sanity checks

Accuracy alone is insufficient — grounding and faithfulness matter more.

🔧 Tech Stack
Layer	Technology
Ingestion	Python
Embeddings	HuggingFace
Vector DB	FAISS
Re-ranking	Cross-Encoder
LLM	Instruction-tuned open-source model
API	FastAPI
Storage	Local
⚠️ Known Failure Modes & Mitigations
Failure Mode	Mitigation
Hallucinations	Strict retrieval grounding
Poor recall	Semantic chunking + domain embeddings
Overconfidence	Confidence gating
Outdated info	Metadata filtering
🧠 Why This Project Matters

This project demonstrates:

Applied ML system design

NLP + embeddings expertise

Responsible LLM usage

Clinical safety awareness

Evaluation maturity

Designed as a real-world ML system, not a demo.

📄 Resume-Ready Bullet

Designed and implemented a Retrieval-Augmented Generation system for clinical literature analysis, integrating domain-specific embeddings, semantic chunking, cross-encoder re-ranking, and citation-grounded LLM responses to support rare disease decision-making while minimizing hallucinations.

⚠️ Disclaimer

This system is for research and educational purposes only.
It does not provide medical advice or diagnoses.

🚀 Next Enhancements

FastAPI inference endpoint

UI for clinicians

Automated citation verification

Temporal filtering of evidence


