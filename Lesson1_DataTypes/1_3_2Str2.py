# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

S = input("Введите строку: ")

# Проверка длины строки
# Если длина < 2,  то пустая строки
if len(S) < 2:
    print("")
else:
    # индексация начала строки - с 0, положительная (1, 2, 3, 4)
    # индексация с конца строки - с -1 (-4, -3, -2, -1)
    print(S[0:2] + S[-2:])