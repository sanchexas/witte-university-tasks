import sys

str = sys.argv[1]
l = str.split(' ')
for i in range(len(l)):
    l[i] = l[i][::-1]
print(" ".join(l))