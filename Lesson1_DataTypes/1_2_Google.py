# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# ввод строки
S = input("Введите строку: ")

# словарь
dict = {}

# перебор букв в веденной строке циклом for
for buk in S:
    # при прохождении цикла каждому новому ключу (букве/символу) присваивается значение 1
    # если ключа (символа) еще нет в dict, присваивается значение 1
    if buk not in dict:
        dict[buk] = 1
    # если ключ (символ) уже есть в dict и встретился еще раз при прохождении цикла for,
    # то у ключа значение становится больше на 1
    else:
        dict[buk] += 1

# печать {ключ: значение}
print(dict)