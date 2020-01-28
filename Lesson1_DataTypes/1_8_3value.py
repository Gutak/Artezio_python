# 8. Write a Python program to find the highest 3 values in a dictionary

# Для вывода max значений
from heapq import nlargest


# Ввод числа элементов словаря (n)
n = int(input("Введите число элементов словаря: "))

# Словарь
MyDict = {}

# Ввод элементов словаря от i до n
for i in range(n):
    MyDict[i] = int(input("Введите значение элемента: "))

# Получить 3 max значения из словаря MyDict
DictMax = nlargest(3, MyDict, key=MyDict.get)

# Печать трех значений в порядке убывания (от 0 до n элементов)
print(DictMax)