import sys

str = sys.argv[1].capitalize().replace(",", ", ")
lastCommaIndex = str.rfind(", ")
result = str[:lastCommaIndex] + ' и' + str[lastCommaIndex+1:]
print(result + ".")
