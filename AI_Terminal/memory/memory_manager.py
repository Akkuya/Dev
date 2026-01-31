# memory/memory_manager.py
import datetime
import os

def save_note(text: str):
    # format timestamp safe for Windows
    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    filename = os.path.join("./memory/vault", f"{timestamp}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)