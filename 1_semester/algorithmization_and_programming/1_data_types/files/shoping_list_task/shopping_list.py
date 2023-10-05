# import os

# ----------------------------------------------------------------------------------------------------------------
    # Вы отправились в магазин и попросили друзей составить список 
    # покупок и прислать его вам. Каждый из друзей написал свой список и в итоге вам прислали три файла:
    #  shopping_list_1.txt, shopping_list_2.txt и shopping_list_3.txt. 
    # Когда вы открыли списки покупок, то сразу заметили, что некоторые товары повторяются, 
    # поэтому вы решили составить свой собственный нормализованный список, где продукты не повторяются и записаны по алфавиту.

    # Напишите программу shopping_list.py, которая читает строки из трех файлов:
    # shopping_list_1.txt, shopping_list_2.txt и shopping_list_3.txt, 
    # а затем создает новый файл shopping_list.txt, в который помещает все прочитанные строки без повторов и в алфавитном порядке.
# ----------------------------------------------------------------------------------------------------------------

# here = os.path.dirname(os.path.abspath(__file__))
# path_1 = os.path.join(here, 'shopping_list_1.txt')
# path_2 = os.path.join(here, 'shopping_list_2.txt')
# path_3 = os.path.join(here, 'shopping_list_3.txt')
# path_for_final = os.path.join(here, 'shopping_list.txt')
# f_1 = open(path_1, encoding="utf-8")
# f_2 = open(path_2, encoding="utf-8")
# f_3 = open(path_3, encoding="utf-8")
# final_txt = open(path_for_final, "w", encoding="utf-8")
f_1 = open("shopping_list_1.txt", encoding="utf-8")
f_2 = open("shopping_list_2.txt", encoding="utf-8")
f_3 = open("shopping_list_3.txt", encoding="utf-8")
final_txt = open("shopping_list.txt", "w", encoding="utf-8")
txt_1 = f_1.read()
txt_2 = f_2.read()
txt_3 = f_3.read()
res_str = txt_1 + "\n" + txt_2 + "\n" + txt_3
res_arr = res_str.split("\n")
dictionary = set(res_arr)
noDublicateArr = list(dictionary)
noDublicateArr.sort()
finalStr = "\n".join(noDublicateArr)
final_txt.write(finalStr)
final_txt.close()