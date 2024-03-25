import sys
password = sys.argv[1]
if(len(password) < 6):
    print("Пароль слишком короткий")
else:
    print("Пароль подходит")