import sys
age = int(sys.argv[1])
hour = int(sys.argv[2])
if hour >= 7 and hour < 22 and age >= 18:
    print('Разрешено')
else:
    print('Запрещено')