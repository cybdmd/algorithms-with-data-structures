# Сортировка вставками

def insert_sort(_array):
    for i in range(len(_array)):
        for j in range(i + 1, len(_array)):
            if _array[j] < _array[i]:
                _array[i], _array[j] = _array[j], _array[i]
    return _array

print(insert_sort([1, 9, 8, 5, 4, 6, 0, 7]))