# controller/controller.py
from models.llm import query_llm

# controller/controller.py
from tools.filesystem import read_file

class Controller:
    def handle(self, user_input: str) -> str:
        if user_input.startswith("read "):
            path = user_input.replace("read ", "")
            return read_file(path)
        return query_llm(user_input)