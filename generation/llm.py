from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "google/flan-t5-small"

print("Loading LLM (FLAN-T5-SMALL)...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def call_llm(system_prompt, user_prompt, max_new_tokens=256):
    full_prompt = f"""
{system_prompt}

{user_prompt}
"""

    inputs = tokenizer(
        full_prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)






