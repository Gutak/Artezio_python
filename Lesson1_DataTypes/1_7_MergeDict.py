# 7. Write a Python script to merge two Python dictionaries

x = {'a': 1, 'b': 2}
y = {'b': 10, 'd': 20}

# Словарь z - копия x
z = x.copy()
# Объединение словарей методом update()
z.update(y)
print(z)
