# 4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3, только возвращает список).


def my_range(start, stop, step):
    list1 = []

    # Цикл пока start <= stop, в list добавляются значения с щагом step
    while start <= stop:
        # Добавляется первое значение в список (start)
        list1.append(start)
        # К значению start прибавляется шаг step и добавляется в список
        start += step

    print(list1)


# range (start, stop, step)
start = int(input("start = "))
stop = int(input("stop = "))
step = int(input("step = "))

my_range(start, stop, step)
