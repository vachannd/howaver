__author__ = "Sudheer"
import typing


def inbetween_number_gen(lower_bound: int, upper_bound: int):
    for x in range(lower_bound, upper_bound + 1):
        yield x


def get_inbetween_factor_count_brute_force(a: typing.List[int], b: typing.List[int]):
    """
    Calculates the number of inbetween factors present between to sets. See <b>between_two_sets<b>
    problem in problems folder of the repository for the explanation.
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
