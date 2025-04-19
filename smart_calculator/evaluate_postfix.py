def evaluate_postfix(postfix_expr):
    stack = []

    for token in postfix_expr:
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                stack.append(left / right)

    return stack.pop()
