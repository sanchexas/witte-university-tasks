import math
import random
from typing import Final
from typing import List

UTF_8: Final[str] = "utf-8"

def readDataFromFile(srcFile: str) -> str:
    data = open(file=srcFile, mode="r", encoding=UTF_8)
    return data.read()

def writeDataToFile(srcFile: str, data: str) -> None:
    open(file=srcFile, mode="w", encoding=UTF_8).write(data)

def removeElementFromString(strOrigin: str, strElemToRemove: str) -> str:
    res: str = ""
    for s in strOrigin: 
        if s != strElemToRemove: 
            res += s
    return res

def customSplit(strOrigin: str, delimiters: str = ' \t\n'):
    res: list = []
    word: str = ""
    for c in strOrigin:
        if c not in delimiters:
            word += c
        elif word:
            res.append(word)
            word = ""
    if word:
        res.append(word)
    return res

def getIntegerByDevide(n1: int, n2: int) -> int:
    return int(n1/n2)

def isEven(n: int) -> bool:
    if(n % 2 == 0): return True 
    else: return False

# order (порядок) : true - по возрастанию, false - по убыванию
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

# order (порядок) : true - по возрастанию, false - по убыванию
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

def getDataArrayFromUnicode(strOrigin: str) -> List[int]:
    arr: list = list(removeElementFromString(strOrigin, " "))
    print(arr)
    res: list = []
    for character in arr:
        res.append(ord(character))
    return res

def arithmeticMeanValue(array: list) -> float:
    sum: int = 0
    for num in array:
        sum += num
    return sum/len(array)

def quadraticValue(array: list) -> float:
    sum: int = 0
    for num in array:
        sum += num**2
    return math.sqrt(sum/len(array))

def toFixedValue(numObj, digitsAfterDot=3):
    return f"{numObj:.{digitsAfterDot}f}"