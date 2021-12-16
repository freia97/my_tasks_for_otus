"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(a, b, c, d):
    res = []
    res.append(a ** 2)
    res.append(b ** 2)
    res.append(c ** 2)
    res.append(d ** 2)
    print(res)
    return res




    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

power_numbers(1, 2, 5, 7)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def odd(lst):
    res = [x for x in lst if x % 2 != 0]
    print(res)
    return res

def even(lst):
    res = [x for x in lst if x % 2 == 0]
    print(res)
    return res

def filter_numbers(nums, options):
    if options == ODD:
        odd(nums)
    elif options == EVEN:
        even(nums)
    elif options == PRIME:
        print(nums)
        return nums


    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
filter_numbers([1, 2, 3], ODD)
filter_numbers([2, 3, 4, 5], EVEN)
filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], PRIME)