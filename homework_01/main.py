"""
Домашнее задание №1
Функции и структуры данных
"""
from math import ceil

def power_numbers(*args):
    """
       функция, которая принимает N целых чисел,
       и возвращает список квадратов этих чисел
       <<< [1, 4, 25, 49]
       """
    res = [x ** 2 for x in args]
    return res


power_numbers(1, 2, 5, 7)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def prime(lst):
    primes = []
    for i in lst:
        if i < 2:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(primes)
    return primes





def odd(lst):
    res = [x for x in lst if x % 2 != 0]
    return res


def even(lst):
    res = [x for x in lst if x % 2 == 0]
    return res


def filter_numbers(nums, options):
    if options == ODD:
        return odd(nums)
    elif options == EVEN:
        return even(nums)
    elif options == PRIME:
        return prime(nums)

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
filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], PRIME)
