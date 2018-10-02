__author__ = "Sudheer"

complexity_map = {1: 1, 2: 2}


def is_incremental_complexity_minimum(x):
    """
    Check whether the increment of complexity of the predecessor is less than the cached value.
    :param x: Current number
    :return: boolean
    """
    return complexity_map[x - 1] + 1 < complexity_map[x]


def is_sum_of_factor_complexities_minimum(x, y):
    """
    Check whether the sum of complexities of the factors is less than the cached value.
    :param x: First factor
    :param y: Second factor
    :return: boolean
    """
    return complexity_map[x] + complexity_map[y] < complexity_map[x * y]


def fill_complexities_for_all_multiples(x, num):
    """
    Cache the complexities for all the multiples of x up to num.
    :param x: Complexities for all multiples of this number are calculated and cached.
    :param num: The upper bound of complexity caching.
    :return: None
    """
    for y in range(2, x + 1):
        if x * y > num:
            break
        else:
            if x * y not in complexity_map or is_sum_of_factor_complexities_minimum(
                x, y
            ):
                complexity_map[x * y] = complexity_map[x] + complexity_map[y]


def get_integer_complexity_sum(num):
    """
    Calculate the sum of all complexities up to :param num inclusive.
    :param num: The number(inclusive) up to which complexities are calculated.
    :return: sum of all complexities up to :param num.
    """
    for x in range(2, num + 1):
        if x not in complexity_map or is_incremental_complexity_minimum(x):
            complexity_map[x] = complexity_map[x - 1] + 1
        fill_complexities_for_all_multiples(x, num)
    return sum(complexity_map.values())
