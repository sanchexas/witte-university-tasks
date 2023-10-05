import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'shopping_list.txt')
f = open(filename, encoding="utf-8") # открыт в режиме чтения
products = f.read().strip().replace("молоко\n", "")  # чтение и удаление лишнего элемента
f.close()

update_file = open(filename, "w", encoding="utf-8") # открытие файла в режиме записи
update_file.write(products) # добавляем в файл строку products, из которой изъят элемент (выше)
update_file.close()