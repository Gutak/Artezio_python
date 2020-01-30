# 3. Написать функцию вычисления факториала числа


def factorial(n):
    # n! = 1 * 2 * ... * (n-1) * n
    fl = 1

    for i in range(1, n + 1):
        fl *= i

    print(f'{n}! = ' + str(fl))


n = int(input("Введите число n: "))
factorial(n)
