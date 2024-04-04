# Посчитать сумму всех чисел массива при помощи while

numbers = [1, 7, 8, 34, 56, 14, 9]
i = 0
summ = 0
while i < len(numbers):
    summ += numbers[i]
    i += 1
print(summ)