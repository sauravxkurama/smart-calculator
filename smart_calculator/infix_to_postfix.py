def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def is_operator(c):
    return c in '+-*/'

def infix_to_postfix(expression):
    output = []
    stack = []

    tokens = expression.split()

    for token in tokens:
        if token.isnumeric() or '.' in token:
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        elif is_operator(token):
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output
