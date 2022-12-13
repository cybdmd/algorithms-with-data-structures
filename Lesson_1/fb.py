"""
Задание:
Пишем алгоритм поиска нужного числа последовательности Фибоначчи.
"""
# рекурсия:

def fb(_num):
    if _num <= 2:
        return 1
    else:
        return fb(_num - 1) + fb(_num - 2)

print(fb(9))

# обычный алгоритм:

def alg_fb(_num):
    if _num <= 2:
        return 1
    else:
        _numbers = list(range(_num))
        _numbers[0] = 1
        _numbers[1] = 1
        for i in range(2,len(_numbers)):
            _numbers[i] = _numbers[i - 1] + _numbers[i - 2]
        return _numbers[_num - 1];

print(alg_fb(9))