def format_expression(expression):
    return ' '.join(expression.strip().split())

def save_to_history(expr, result):
    with open("history.txt", "a") as file:
        file.write(f"{expr} = {result}\n")

def load_history():
    try:
        with open("history.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
