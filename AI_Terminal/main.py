# main.py
from controller.controller import Controller
from interface.cli import run_cli
from memory.memory_manager import save_note

# initialize controller
controller = Controller()

# start CLI
def handler(user_input: str):
    # phase 0: save every input as a note (optional)
    save_note(user_input)
    return controller.handle(user_input)

if __name__ == "__main__":
    print("=== AI Assistant Phase 0 ===")
    print("Type 'exit' to quit.\n")
    run_cli(handler)