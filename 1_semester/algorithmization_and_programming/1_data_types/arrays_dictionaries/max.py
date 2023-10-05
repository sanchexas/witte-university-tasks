import sys
arr = sys.argv[1:]
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(max(arr))