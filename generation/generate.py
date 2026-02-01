from generation.prompt import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from generation.llm import call_llm

def format_evidence(reranked_chunks, metadata):
    evidence_blocks = []
    for i, (_, (_, idx)) in enumerate(reranked_chunks, 1):
        text = metadata[idx]["text"]
        evidence_blocks.append(f"[Paper {i}] {text}")
    return "\n\n".join(evidence_blocks)

def generate_answer(question, reranked_chunks, metadata):
    evidence = format_evidence(reranked_chunks, metadata)

    user_prompt = USER_PROMPT_TEMPLATE.format(
        question=question,
        evidence=evidence
    )

    return call_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt
    )

