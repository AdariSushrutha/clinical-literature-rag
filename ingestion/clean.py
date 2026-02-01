import re
from pathlib import Path

def clean_text(text: str) -> str:
    # Remove references section
    text = re.split(r'\nreferences\n', text, flags=re.IGNORECASE)[0]

    # Remove figure/table mentions
    text = re.sub(r'figure\s+\d+|table\s+\d+', '', text, flags=re.IGNORECASE)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

if __name__ == "__main__":
    raw_dir = Path("data/raw")
    output_file = Path("data/processed/cleaned.txt")

    all_text = []

    for file in raw_dir.glob("*.txt"):
        print(f"Cleaning {file.name}")
        all_text.append(clean_text(file.read_text(encoding="utf-8")))

    if not all_text:
        raise RuntimeError("No .txt files found in data/raw")

    output_file.write_text("\n\n".join(all_text), encoding="utf-8")
    print(" cleaned.txt created")

