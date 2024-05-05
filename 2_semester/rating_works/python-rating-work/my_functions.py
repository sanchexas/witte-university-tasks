# Работа выполнена студентом 1-го курса группы "о.ИЗДтс 23.1/Б3-23" университета МУИВ
# Санчес-Перес Сергеем Евгеньевичем
# Мой GitHub - https://github.com/sanchexas

import math
import random
from typing import Final
from typing import List

UTF_8: Final[str] = "utf-8"

# -Чтение текста из файла
def readDataFromFile(srcFile: str) -> str:
    data = open(file=srcFile, mode="r", encoding=UTF_8)
    return data.read()

# -Добавление текста в файл
def writeDataToFile(srcFile: str, data: str) -> None:
    open(file=srcFile, mode="w", encoding=UTF_8).write(data)

# -Удалить элемент из строки
def removeElementFromString(strOrigin: str, strElemToRemove: str) -> str:
    res: str = ""
    for s in strOrigin: 
        if s != strElemToRemove: 
            res += s
    return res

# -Кастомный split()
def customSplit(strOrigin: str, delimiters: str) -> List[str]:
    res: list = []
    word: str = ""
    for character in strOrigin:
        if character not in delimiters:
            word += character
        elif word:
            res.append(word)
            word = ""
    if word:
        res.append(word)
    return res

# -Деление
def getIntegerByDevide(n1: int, n2: int) -> int:
    return int(n1/n2)

# -Проверка числа на четность
def isEven(n: int) -> bool:
    if(n % 2 == 0): return True 
    else: return False

# -Алгоритм "быстрой сортировки" (Хоара)
# --order (порядок) : true - по возрастанию, false - по убыванию
# TODO Как-то можно оптимизировать данную функцию в плане условия с порядком (if order), но мне лень...
def quickSort(numsArray: List[int], order: bool) -> List[int]:
    if len(numsArray) <= 1:
        return numsArray
    else:
        pivot = random.choice(numsArray)
        left: list = []
        medium: list = []
        right: list = []
        if(order == True):
            for elem in numsArray:
                if elem < pivot:
                    left.append(elem) 
                elif elem > pivot: 
                    right.append(elem) 
                else: 
                    medium.append(elem)
        else: 
            for elem in numsArray:
                if elem > pivot:
                    left.append(elem) 
                elif elem < pivot: 
                    right.append(elem) 
                else: 
                    medium.append(elem)
        return quickSort(left, order) + medium + quickSort(right, order)

# -Алгоритм сортировки по методу "пузырька"
# --order (порядок) : true - по возрастанию, false - по убыванию
# TODO Как-то можно оптимизировать данную функцию в плане условия с порядком (if order), но мне лень...
def bubbleSort(numsArray: List[int], order: bool) -> List[int]:
    n = len(numsArray)
    if(order):
        for i in range(n):
            for j in range(0, n - i - 1):
                if numsArray[j] > numsArray[j + 1]:
                    numsArray[j], numsArray[j + 1] = numsArray[j + 1], numsArray[j]
    else:
        for i in range(n):
            for j in range(0, n - i - 1):
                if numsArray[j] < numsArray[j + 1]:
                    numsArray[j], numsArray[j + 1] = numsArray[j + 1], numsArray[j]
    return numsArray

# -Формирование набора данных из кодов Юникода
def getUnicodeDataArray(strOrigin: str) -> List[int]:
    arr: list = list(strOrigin)
    res: list = []
    for character in arr:
        res.append(ord(character))
    return res

# -Вычисление среднего арифметического значения набора данных
def arithmeticMeanValue(array: list) -> float:
    sum: int = 0
    for num in array:
        sum += num
    return sum/len(array)

# -Вычисление среднего квадратического значения набора данных
def quadraticValue(array: list) -> float:
    sum: int = 0
    for num in array:
        sum += num**2
    return math.sqrt(sum/len(array))

# -Округление значения до трех (по умолчанию) знаков после точки
def toFixedValue(numObj, digitsAfterDot: int = 3) -> float:
    return float(f"{numObj:.{digitsAfterDot}f}")