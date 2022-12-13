"""
Задание:
Необходимо написать алгоритм поиска всех доступных комбинаций
(посчитать количество) для количества кубиков K с количеством граней N.
"""
# Простой вариант (количество кубиков 4).
def square_comb(faces):
    _count = 0
    for i in range(1, faces + 1):
        for j in range(1, faces + 1):
            for k in range(1, faces + 1):
                for l in range(1, faces + 1):
                    _count += 1
    return _count

# print(square_comb(6))

# Сложный вариант - количество кубиков задается условием.

def combination_count(_count, _faces):
    if _count > 0:
        return recursive_counter(1, _count, _faces)
    else:
        return 0

def recursive_counter(_depth, _max_depth, _faces):
    _count = 0
    for i in range(1, _faces + 1):
        if _depth == _max_depth:
            _count += 1
        else:
            _count += recursive_counter(_depth + 1, _max_depth, _faces)
    return _count

print(combination_count(4, 6))