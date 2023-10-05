import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'shopping_list.txt')
f = open(filename, encoding="utf-8")
products = f.read()
print(products)