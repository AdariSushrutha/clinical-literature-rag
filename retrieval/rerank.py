import json
from sentence_transformers import CrossEncoder

def rerank(query, retrieved, metadata, top_n=5):
    """
    query: str
    retrieved: list of (score, idx) from dense retrieval
    metadata: loaded metadata.json
    """
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    pairs = []
    for _, idx in retrieved:
        text = metadata[idx].get("text", None)
        if text is None:
            raise ValueError("Chunk text missing from metadata")
        pairs.append((query, text))

    scores = model.predict(pairs)

    reranked = list(zip(scores, retrieved))
    reranked.sort(key=lambda x: x[0], reverse=True)

    return reranked[:top_n]

