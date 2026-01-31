# tools/filesystem.py
import os

def read_file(path: str) -> str:
    if not os.path.exists(path):
        return "File not found."
    with open(path, "r", encoding="utf-8") as f:
        return f.read()