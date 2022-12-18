# Сортировка пузырьком

from timeit import timeit

def bubble_sort(_array):
    for i in range(len(_array)):
        for j in range(len(_array) - 1):
            if _array[j] > _array[j + 1]:
                _array[j], _array[j + 1] = _array[j + 1], _array[j]
    return _array

print(timeit("bubble_sort([100, 1, 9, 8, 5, 4, 6, 0, 7])", globals=globals(), number=1000))
print(bubble_sort([100, 1, 9, 8, 5, 4, 6, 0, 7]))