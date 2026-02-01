import re
import json
from pathlib import Path

SECTION_HEADERS = [
    "Introduction",
    "Clinical features",
    "Diagnosis",
    "Differential diagnosis",
    "Disease progression",
    "Prognosis",
    "Management",
    "Treatment",
    "Pathophysiology",
    "Epidemiology"
]

def split_into_sentences(text: str):
    # Simple sentence splitter (robust enough for medical prose)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 0]

def chunk_by_sections(text: str, max_words: int = 400, min_words: int = 80):
    pattern = "(" + "|".join(SECTION_HEADERS) + ")"
    splits = re.split(pattern, text, flags=re.IGNORECASE)

    chunks = []

    for i in range(1, len(splits), 2):
        section = splits[i].lower()
        content = splits[i + 1]

        sentences = split_into_sentences(content)

        current_chunk = []
        current_word_count = 0

        for sentence in sentences:
            words = sentence.split()
            current_chunk.append(sentence)
            current_word_count += len(words)

            if current_word_count >= max_words:
                if current_word_count >= min_words:
                    chunks.append({
                        "section": section,
                        "text": " ".join(current_chunk)
                    })
                current_chunk = []
                current_word_count = 0

        # Add remainder
        if current_word_count >= min_words:
            chunks.append({
                "section": section,
                "text": " ".join(current_chunk)
            })

    return chunks


if __name__ == "__main__":
    input_path = Path("data/processed/cleaned.txt")
    output_path = Path("data/processed/chunks.json")

    text = input_path.read_text(encoding="utf-8")
    chunks = chunk_by_sections(text)

    output_path.write_text(
        json.dumps(chunks, indent=2),
        encoding="utf-8"
    )

    print(f" Created {len(chunks)} refined semantic chunks")

