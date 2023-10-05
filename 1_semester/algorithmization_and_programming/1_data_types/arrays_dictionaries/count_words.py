import re
import sys

s = sys.argv[1]
words = re.findall(r'\b\w+\b', s)
print(len(words))