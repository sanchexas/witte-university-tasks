# Работа выполнена студентом 1-го курса группы "о.ИЗДтс 23.1/Б3-23" университета МУИВ
# Санчес-Перес Сергеем Евгеньевичем
# Мой GitHub - https://github.com/sanchexas

# -Кастомные функции
from my_functions import *
from typing import List

# -Получение текста из файла
sourceFileData: str = readDataFromFile('source_data.txt')
# -Разбитие строки на массив [ФИО, ID]
fioAndIdList: list = customSplit(sourceFileData, '\n')
# -Присваивание переменной ФИО
fio: str = fioAndIdList[0]
# -Присваивание переменной ID
id: int = int(fioAndIdList[1])
# -Удаление пробелов в ФИО
removedSpacesFromFio: str = removeElementFromString(fio, ' ')
# -Деление ID на длину ФИО (без учета пробелов)
devideIdByFioResult: int = getIntegerByDevide(id, len(removedSpacesFromFio))
# -Формирование набора данных из кодов Юникода
dataList: List[int] = getUnicodeDataArray(removedSpacesFromFio)
# -Копирование несортированного набора данных для будущего использования для записи в файл результата
unSortedDataList: List[int] = dataList[:]
# -Проверка на то, является ли результат деления ID на длину ФИО четным
isDevideResultEven: bool = isEven(devideIdByFioResult)
# -Алгоритм "быстрой сортировки" (Хоара) 
quickSortResult: List[int] = quickSort(dataList, isDevideResultEven)
# -Алгоритм сортировки по методу "пузырька"
bubbleSortResult: List[int] = bubbleSort(dataList, isDevideResultEven)
# -Вычисление среднего арифметического значения набора данных
arithmeticMeanResult: float = arithmeticMeanValue(quickSortResult)
# -Вычисление среднего квадратического значения набора данных
quadraticResult: float = quadraticValue(bubbleSortResult)
# -Порядок сортировки
orderMessage: float = 'по возрастанию' if isDevideResultEven else 'по убыванию'
# -Запись в файл:
# --функция toFixedValue - округляет значение до трех (по умолчанию) знаков после точки
writeDataToFile('result.txt', f'1. Исходные данные: {fio}; ID: {id}\n2. {devideIdByFioResult}\n3. Направление сортировки {orderMessage}, так как число {devideIdByFioResult} - {"четное" if isDevideResultEven else "нечетное"}\n4. Набор данных: {unSortedDataList}\n5. Отсортированный {orderMessage} набор данных {quickSortResult}\n6. Среднее арифметическое значение: {toFixedValue(arithmeticMeanResult)}\n7. Среднее квадратическое значение: {toFixedValue(quadraticResult, 3) }')