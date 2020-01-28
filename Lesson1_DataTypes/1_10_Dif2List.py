# 10. Write a Python program to get the difference between the two lists

# Ввод числа элементов списка
n1 = int(input("Введите число элементов списка 1, n1 = "))
# Список
list1 = []

# Ввод элементов списка от i до n
for i in range(n1):
    list1.append(input("Введите элемент списка 1: "))

n2 = int(input("Введите число элементов скиска 2, n2 = "))
list2 = []

for i in range(n2):
    list2.append(input("Введите элемент списка 2: "))

# list3 = list(set(list1) - set(list2))
set1 = set(list1)
set2 = set(list2)
list3 = list(set1.difference(set2))
print(list3)
