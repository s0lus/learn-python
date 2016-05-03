"""
Медиана - это числовое значение, которое делит сортированый массив чисел на большую и меньшую половины.
В сортированом массиве с нечетным числом элементов медиана - это число в середине массива.
Для массива с четным числом элементов, где нет одного элемента точно посередине,
медиана - это среднее значение двух чисел, находящихся в середине массива.
В этой задаче дан непустой массив натуральных чисел.
Вам необходимо найти медиану данного массива.

ПРИМЕР:
checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5
"""


def checkio(array):
    sorted_array = sorted(array)
    mid = int(len(sorted_array) / 2)
    if len(array) % 2 == 0:
        return (sorted_array[mid] + sorted_array[mid - 1]) / 2
    else:
        return sorted_array[mid]



print(checkio([1, 2, 3, 4, 5]))
print(checkio([3, 1, 2, 5, 3]))
print(checkio([1, 300, 2, 200, 1]))
print(checkio([3, 6, 20, 99, 10, 15]))