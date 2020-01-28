# 5. You are given with 3 sets, find if third set is a subset of the first and the second sets
# Input: set([1,2]), set([2,3), set([2])
# Expected result: True
# Input: set([1,2]), set([3,4), set([5])
# Expected result: False


set1 = {1, 2}
set2 = {2, 3}
set3 = {2}

# определение подмножества
# sub_set.issubset(set_mn)
# Функция возвращает значение True, если:
# 1. множества sub_set и set_mn равны
# 2. мн-во sub_set - это подмножество множества set_mn

# мн-во set3 - это подмножество множества set1?
x31 = set3.issubset(set1)
# мн-во set3 - это подмножество множества set2?
x32 = set3.issubset(set2)
print("Мн-во set3 - это подмножество множества set1? " + str(x31), '\n' + "Мн-во set3 - это подмножество множества set2? " + str(x32))
