__author__ = "Sudheer"

import functools


# https://docs.python.org/3/library/functools.html#functools.lru_cache
@functools.lru_cache(maxsize=3)
def sub_factorial(n: int) -> int:
    """
    Calculates the subfactorial of the integer 'n'.
    :param n: integer to which the subfactorial will be calculated.
    :return: subfactorial of n.
    """
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (sub_factorial(n - 1) + sub_factorial(n - 2))
