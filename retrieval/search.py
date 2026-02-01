import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

ALLOWED_SECTIONS_FOR_DIAGNOSIS = {
    "diagnosis",
    "clinical_features",
    "investigations",
    "differential_diagnosis"
}

def retrieve(query, k=10):
    index = faiss.read_index("data/processed/faiss.index")
    embeddings = np.load("data/processed/embeddings.npy")
    metadata = json.load(open("data/processed/metadata.json"))

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    q_emb = model.encode([query], normalize_embeddings=True)

    scores, idxs = index.search(q_emb, k=30)  # over-retrieve

    filtered = []
    for score, idx in zip(scores[0], idxs[0]):
        section = metadata[idx]["section"].lower()
        if section in ALLOWED_SECTIONS_FOR_DIAGNOSIS:
            filtered.append((score, idx))
        if len(filtered) == k:
            break

    return filtered, metadata

