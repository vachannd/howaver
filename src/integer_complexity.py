import sys

__author__ = "Sudheer"

# TODO
integer_complexity_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


def get_factors(value):
    root = int(value ** 0.5)
    for x in range(root, 1, -1):
        if value % x == 0:
            yield x, value // x


def get_integer_complexity(num):
    if num in integer_complexity_map.keys():
        return integer_complexity_map[num]
    else:
        min_integer_complexity = sys.maxsize
        for x in get_factors(num):
            current_integer_complexity = get_integer_complexity(x[0]) + get_integer_complexity(x[1])
            if current_integer_complexity < min_integer_complexity:
                min_integer_complexity = current_integer_complexity
        else:
            integer_complexity_map[num] = min(get_integer_complexity(num - 1) + 1, min_integer_complexity)
        return integer_complexity_map[num]
