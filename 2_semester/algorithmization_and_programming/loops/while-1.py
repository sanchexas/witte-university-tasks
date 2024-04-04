# Запушить нечетные числа от 11 до 27 в массив.
i = 11
numbers = []
while(i <= 27):
    if(i % 2 != 0):
        numbers.append(i)
    i += 1
    