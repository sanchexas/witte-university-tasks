import sys

text = list(sys.argv[1])
for i in text[::-1]:
    if i in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
        text.remove(i)
print(str(''.join(text)))