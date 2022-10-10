
from inspect import stack


def isBalanced(s:str) -> bool:
    stack = []
    
    for char in s:
        if stack and stack[-1] == '(' and char == ')':
            stack.pop()
        elif stack and stack[-1] == '[' and char == ']':
            stack.pop()
        elif stack and stack[-1] == '{' and char == '}':
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return False
    return True

print(isBalanced('()[]{}'))
print(isBalanced('[{()}]'))
