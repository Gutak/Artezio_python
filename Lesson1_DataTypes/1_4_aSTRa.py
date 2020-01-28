# 4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2



# Ввод количества строк
kol = input("Введите количество строк: ")
# Строка в int
kol = int(kol)
i = 0

# Число строк, где вначалеи и в конце одинаковые символы (изначально - 0)
ch = 0

# Ввод такого кол-ва строк, сколько пользователь указал в "kol"
for i in range(kol):

    S = input("Введите строку: ")

    # Длина строки < 2 символов
    if len(S) < 2:
        print("Строка должна быть больше 1го символа")

    # Длина строки >= 2х символов
    else:
        # Первый символ строки = последнему
        # Символы начала строки (0, 1, 2), конца - (-1, -2, -3)
        if S[0] == S[-1]:
            # Если первый и последний символ совпадают, то количество строк становится на 1 больше (изначально 0)
            ch += 1

print(ch)
