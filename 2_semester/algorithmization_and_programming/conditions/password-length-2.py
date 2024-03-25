import sys
password = sys.argv[1]
psLen = len(password)
if(psLen < 6):
    print('Пароль слишком короткий')
elif(psLen > 8 ):
    print('Пароль подходит')
else:
    print('Хорошо, но можно и лучше')
