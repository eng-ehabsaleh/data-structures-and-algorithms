def validate_brackets(s):
    if len(s) % 2 != 0:
        return False
    start = set('[{(')
    match = set([('[', ']'), ('{', '}'), ('(', ')')])
    stack = []
    for p in s:
        if p in start:
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            if p in start:
                L = stack.pop()
                if (L, p) not in match:
                    return False
    return True


print(validate_brackets("{(}"))
print(validate_brackets("()[[Extra Characters]]"))
print(validate_brackets("(){}[[]]"))
print(validate_brackets("(]("))
print(validate_brackets("{(})"))
