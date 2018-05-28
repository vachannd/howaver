import math

__author__ = "Sudheer"

# TODO
integer_complexity_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


def get_min_factors(value):
    root = int(math.sqrt(value))
    factor1, factor2 = 0, 0
    for x in range(root, 0, -1):
        if value % x == 0:
            factor1, factor2 = x, value // x
            break
    return factor1, factor2


def get_integer_complexity(num):
    if num in integer_complexity_map.keys():
        return integer_complexity_map[num]
    else:
        factor1, factor2 = get_min_factors(num)
        if factor1 == num or factor2 == num:
            integer_complexity_map[num] = get_integer_complexity(num - 1) + 1
        else:
            integer_complexity_map[num] = min(get_integer_complexity(num - 1) + 1,
                                              get_integer_complexity(factor1) + get_integer_complexity(factor2))

        return integer_complexity_map[num]


# TODO
print(get_integer_complexity(92))
