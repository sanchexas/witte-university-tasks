import sys
 
 
def foo(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 0
            stack.pop()
    if not stack:
        return 1
    else:
        return 0
 
 
s = sys.argv[1]
print(foo(s))