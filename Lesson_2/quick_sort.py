# Быстрая сортировка (quicksort)
import random

def quick_sort(_array):
    if len(_array) <= 1:
        return _array
    else:
        q = random.choice(_array)
        s_nums = []
        l_nums = []
        e_nums = []
        for n in _array:
            if n < q:
                s_nums.append(n)
            elif n > q:
                l_nums.append(n)
            else:
                e_nums.append(n)
    return quick_sort(s_nums) + e_nums + quick_sort(l_nums)

print(quick_sort([100, 1, 9, 8, 5, 4, 6, 0, 7]))