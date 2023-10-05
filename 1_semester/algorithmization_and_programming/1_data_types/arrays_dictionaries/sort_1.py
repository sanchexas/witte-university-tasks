import sys
str = ''
arr = sorted(sys.argv[1])
for i in range(len(arr)):
    str += arr[i]
print(str)