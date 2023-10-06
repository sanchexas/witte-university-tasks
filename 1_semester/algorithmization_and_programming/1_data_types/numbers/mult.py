import sys

num = int(sys.argv[1])

for i in range(1,10):
    res = num * i
    print(f"{num} x {i} = {res}")