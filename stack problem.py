def BalancedBrackets(Str):
    """
    Function to check if the parenthesis is balanced or not.
    """
    stack = []
    for parenthesis in Str:
        if parenthesis == '{' or parenthesis == '(' or parenthesis == '[':
            stack.append(parenthesis)
        elif parenthesis == '}' or parenthesis == ')' or parenthesis == ']':
            if len(stack) < 1:
                return False
            last_item = stack.pop()
            if not Compare(last_item, parenthesis):
                return False
    if len(stack) != 0:
        return False

    return True


def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False


print(BalancedBrackets("(){}[]"))




