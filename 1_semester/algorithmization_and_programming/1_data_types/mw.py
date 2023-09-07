import sys

m = sys.argv[1].count('m')
w = sys.argv[1].count('w')

print(f"m ({m}) {'*' * m}")
print(f"w ({w}) {'*' * w}")