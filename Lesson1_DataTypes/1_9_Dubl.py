# 9. Write a Python program to remove duplicates from a list
from typing import Tuple

n = int(input("Введите число элементов списка: "))

# Список
MyList = []

# Ввод элементов списка от i до n
for i in range(n):
    # Ввод элементов списка с клапвиатуры
    MyList.append(input("Введите элемент списка: "))

print(list(set(MyList)))
