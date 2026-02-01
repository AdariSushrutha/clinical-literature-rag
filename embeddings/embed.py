import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

CHUNKS_PATH = Path("data/processed/chunks.json")
EMBEDDINGS_PATH = Path("data/processed/embeddings.npy")
METADATA_PATH = Path("data/processed/metadata.json")

def main():
    print("Loading chunks...")
    chunks = json.loads(CHUNKS_PATH.read_text())

    texts = [c["text"] for c in chunks]
    metadata = [
    {
        "section": c["section"],
        "text": c["text"],
        "chunk_id": i
    }
    for i, c in enumerate(chunks)
]

    print("Loading embedding model...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    print("Embedding chunks...")
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    print("Saving embeddings...")
    np.save(EMBEDDINGS_PATH, embeddings)
    METADATA_PATH.write_text(json.dumps(metadata, indent=2))

    print(f" Embedded {len(embeddings)} chunks")

if __name__ == "__main__":
    main()

