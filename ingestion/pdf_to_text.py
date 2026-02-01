import fitz  # PyMuPDF
from pathlib import Path

RAW_DIR = Path("data/raw")

def pdf_to_text(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        pages.append(page.get_text())
    return "\n".join(pages)

if __name__ == "__main__":
    pdfs = list(RAW_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found.")
        raise SystemExit(0)

    for pdf in pdfs:
        print(f"Converting {pdf.name} ...")
        text = pdf_to_text(pdf)
        txt_path = pdf.with_suffix(".txt")
        txt_path.write_text(text, encoding="utf-8")

    print(" PDF → TXT conversion complete")

