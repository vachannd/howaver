__author__ = "Sudheer"

from src import integer_complexity

# Complexities of the first hundred integers.
expected_integer_complexities = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 7, 8, 8, 8, 8, 9, 8, 9, 9, 9, 10, 11,
                                 9, 10, 10, 9, 10, 11, 10, 11, 10, 11, 11, 11, 10, 11, 11, 11, 11,
                                 12, 11, 12, 12, 11, 12, 13, 11, 12, 12, 12, 12, 13, 11, 12, 12,
                                 12, 13, 14, 12, 13, 13, 12, 12, 13, 13, 14, 13, 14, 13, 14, 12,
                                 13, 13, 13, 13, 14, 13, 14, 13,
                                 12, 13, 14, 13, 14, 14, 14, 14, 15, 13, 14, 14, 14, 15, 14, 13, 14, 14, 14, 14]


def verify_first_hundred_complexities():
    assert 1113 == integer_complexity.get_integer_complexity_sum(100)


def verify_sum_of_first_thousand_complexities():
    assert 18274 == integer_complexity.get_integer_complexity_sum(1000)


def verify_sum_of_million_complexities():
    """Time this test. It should not take more than 5 seconds. If it does, improve the code."""
    assert 39519866 == integer_complexity.get_integer_complexity_sum(1000000)

def test_integer_complexity():
    verify_sum_of_million_complexities()
