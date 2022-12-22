# Сортировка кучей

from timeit import timeit

def heap_sort(_array):
    build_max_heap(_array)
    for i in range(len(_array) - 1, 0, -1):
        _array[0], _array[i] = _array[i], _array[0]
        max_heapify(_array, _index=0, _size=i)
    return _array

def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(_array):
    _length = len(_array)
    _start = parent(_length - 1)
    while _start >= 0:
        max_heapify(_array, _index=_start, _size=_length)
        _start -= 1


def max_heapify(_array, _index, _size):
    l = left(_index)
    r = right(_index)
    if l < _size and _array[l] > _array[_index]:
        _largest = l
    else:
        _largest = _index
    if r < _size and _array[r] > _array[_largest]:
        _largest = r
    if _largest != _index:
        _array[_largest], _array[_index] = _array[_index], _array[_largest]
        max_heapify(_array, _largest, _size)

'''
_array = input('Enter the list of numbers: ').split()
_array = [int(x) for x in _array]
heap_sort(_array)
print('Sorted list: ', end='')
print(_array)
'''

print(timeit("heap_sort([100, 1, 9, 8, 5, 4, 6, 0, 7])", globals=globals(), number=1000))
print(heap_sort([100, 1, 9, 8, 5, 4, 6, 0, 7]))
