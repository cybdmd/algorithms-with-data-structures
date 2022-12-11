"""
Задание:
Написать алгоритм поиска простых чисел (делятся только на себя и на 1)
в диапазоне от 1 до N.
"""

def simple_num(n):
    simple_list = []
    _flag = True
    for i in range(2, n + 1):
        _flag = True
        for j in range(2, i):
            if i % j == 0:
                _flag = False
                break
        if _flag:
            simple_list.append(i)
    return simple_list

print(simple_num(11))