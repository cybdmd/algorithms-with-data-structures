# Сортировка выбором

def choice_sort(_array):
    for i in range(len(_array)):
        _min_position = i
        for j in range(i + 1, len(_array)):
            if _array[j] < _array[_min_position]:
                _min_position = j
        if _min_position != i:
            _array[i], _array[_min_position] = _array[_min_position], _array[i]
    return _array

print(choice_sort([1, 9, 8, 5, 4, 6, 0, 7]))