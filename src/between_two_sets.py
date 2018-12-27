__author__ = "Sudheer"

import functools
import math
import typing


def inbetween_number_gen(lower_bound: int, upper_bound: int):
    for x in range(lower_bound, upper_bound + 1):
        yield x


def _lcm_of_sequence(sequence: typing.List[int]):
    """
    This method is only educational. It will break for large numbers.
    :param sequence: List of integers
    :return: LCM of a list
    """
    return functools.reduce(
        lambda x, y: (
            lambda a, b: next(
                i for i in range(max(a, b), a * b + 1) if i % a == 0 and i % b == 0
            )
        )(x, y),
        sequence,
    )


def lcm_of_sequence(sequence: typing.List[int]):
    return functools.reduce(lambda a, b: a * b // math.gcd(a, b), sequence)


def gcd_of_sequence(sequence: typing.List[int]):
    return functools.reduce(math.gcd, sequence)


def get_inbetween_factor_count_brute_force(a: typing.List[int], b: typing.List[int]):
    """
    Calculates the number of inbetween factors present between to sets. See <b>between_two_sets<b>
    problem in problems folder of the repository for the explanation.
    This is a Brute Force solution.
    :param a: List of integers
    :param b: List of integers
    :return: Count of inbetween factors.
    """
    inbetween_factors = []
    for x in inbetween_number_gen(a[-1], b[0]):
        for array_one_ele in a:
            if x % array_one_ele:
                break
        else:
            for array_two_ele in b:
                if array_two_ele % x:
                    break
            else:
                inbetween_factors.append(x)
    return len(inbetween_factors)


def get_inbetween_factor_count_lcm_gcd(a: typing.List[int], b: typing.List[int]):
    """
    Calculates the number of inbetween factors present between to sets. See <b>between_two_sets<b>
    problem in problems folder of the repository for the explanation.
    :param a: List of integers
    :param b: List of integers
    :return: Count of inbetween factors.
    """
    if a[-1] > b[0]:
        return 0
    inbetween_factors = []
    lcm_array_one = _lcm_of_sequence(
        a
    )  # LCM of a list with large numbers will take very long.
    gcd_array_two = gcd_of_sequence(b)
    for x in inbetween_number_gen(lcm_array_one, gcd_array_two):
        for array_one_ele in a:
            if x % array_one_ele:
                break
        else:
            for array_two_ele in b:
                if array_two_ele % x:
                    break
            else:
                inbetween_factors.append(x)

    return len(inbetween_factors)


def get_inbetween_factor_count_optimal(a: typing.List[int], b: typing.List[int]):
    """
    Calculates the number of inbetween factors present between to sets. See <b>between_two_sets<b>
    problem in problems folder of the repository for the explanation.
    :param a: List of integers
    :param b: List of integers
    :return: Count of inbetween factors.
    """
    lcm_array_one = lcm_of_sequence(a)
    gcd_array_two = gcd_of_sequence(b)
    inbetween_factor_count = 0
    if gcd_array_two % lcm_array_one == 0:
        i = 1
        greatest_inbetween_factor = gcd_array_two // lcm_array_one
        while i * i <= greatest_inbetween_factor:
            if greatest_inbetween_factor % i == 0:
                inbetween_factor_count += 1
                if i * i != greatest_inbetween_factor:
                    inbetween_factor_count += 1
            i += 1

    return inbetween_factor_count
