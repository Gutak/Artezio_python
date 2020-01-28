# 1. You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalized correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
# Input Format:A single line of input containing the full name, S.
# Constraints:* 0 < len(S) < 1000*
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized.
# Example 12abc when capitalized remains 12abc.
# Output Format:Print the capitalized string, S.


# Ввод имени и фамилии
S = input("Введите имя и фамилию: ")

# all(iterable) - возвращает True, если все элементы iterable имеют значение True
# iterable (итерируемый) - объект, предоставляющий возможность поочередного прохода по своим элементам
# c.isalnum() - состоит ли строка из цифр или букв
# c.isspace() - состоит ли строка из неотображаемых символов (пробел, новая строка и т.д.)
result = all(c.isalnum() or c.isspace() for c in S)
# result == False
if not result:
    print("ФИО не должно содержать спец. символы")
# Если нет спец символов
else:
    # Длина строки от 1 до 999 символов
    if 0 < len(S) < 1000:
        # Вывод слов с заглавной буквы
        print(S.title())
    elif len(S) == 0:
        print("Введите имя и фамилию")
    else:
        print("Превышена длина строки")


