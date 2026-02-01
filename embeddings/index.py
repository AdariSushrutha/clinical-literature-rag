import faiss
import numpy as np
from pathlib import Path

EMBEDDINGS_PATH = Path("data/processed/embeddings.npy")
INDEX_PATH = Path("data/processed/faiss.index")

def main():
    embeddings = np.load(EMBEDDINGS_PATH)
    dim = embeddings.shape[1]

    print("Building FAISS index...")
    index = faiss.IndexFlatIP(dim)  # Inner product = cosine similarity (normalized)

    index.add(embeddings)

    faiss.write_index(index, str(INDEX_PATH))
    print(f" FAISS index built with {index.ntotal} vectors")

if __name__ == "__main__":
    main()

