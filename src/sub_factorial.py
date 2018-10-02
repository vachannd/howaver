__author__ = "Sudheer"

import functools


@functools.lru_cache(maxsize=3)
def sub_factorial(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (sub_factorial(n - 1) + sub_factorial(n - 2))
