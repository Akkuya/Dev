# interface/cli.py
def run_cli(handler):
    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print(handler(user_input))