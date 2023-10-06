import sys
 
 
def foo(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return 0
    return 1
 
 
print(foo(sys.argv[1:]))