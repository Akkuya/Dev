# models/llm.py
import subprocess

def query_llm(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8"  # <-- force UTF-8 decoding
    )
    return result.stdout.strip()