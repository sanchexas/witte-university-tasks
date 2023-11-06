# Работа выполнена студентом Московского Университета Имени Витте (МУИВ)
# Санчес-Перес Сергеем Е.
# ВАРИАНТ - 17
import os
import cmath
# Без модуля 'os' открытие файлов почему-то не работает, но известно, что можно обойтись без 'os'
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
UTF_8 = 'utf-8'
GET_SOURCE_DATA_FILE = os.path.join(CURRENT_FOLDER, 'source_data.txt')
GET_RESULT_FILE = os.path.join(CURRENT_FOLDER, 'result.txt')
opennedSourceDataFile = open(GET_SOURCE_DATA_FILE, 'r', encoding=UTF_8)
opennedResultFile = open(GET_RESULT_FILE, 'w', encoding=UTF_8)
# Чтение, удаление из строки 'x=', разбитие строки на массив оставшихся строковых значений
sourceDataNums = opennedSourceDataFile.read().replace('x=', '').split('\n')
# Функция, вычисляющая Y
def calculateY(x):
    # Не забываем приобразовать в int
    x = int(x)
    if x < -4:
        return ((16 * x ** 6 - 6 * x ** 2 - 22) ** 6) + 23 * x ** 3 / ((34 * x ** 5 + x ** 3) ** 5 + (18 * x ** 2 + 70) ** 4)
    elif -4 <= x < 0:
        return (cmath.sqrt((74 * x ** 7 + 80 * x ** 2 + 28) ** 5)) - 45 * x ** 7 / ((73 * x ** 4 + x ** 2) ** 5 + (94 * x ** 2 - 34) ** 6)
    elif x >= 0:
        return ((17 * x ** 4 + 17 * x ** 2 +  62) ** 4 - 91 * x ** 5) / ((36 * x ** 8 - x ** 3) ** 4 + cmath.sqrt((76 * x - 61) ** 3))
# Вызов 'calculateY(x)' для каждого X массива 'sourceDataNums' и запись результата функции в файл result.txt
for x in sourceDataNums:
    result = f'При x = {x} значение y = {calculateY(x):.3f}'
    opennedResultFile.write(result + '\n')