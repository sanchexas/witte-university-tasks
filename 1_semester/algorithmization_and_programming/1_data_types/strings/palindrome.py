import sys 

str = sys.argv[1]

if str == str[::-1]:
    print(1)
else:
    print(0)