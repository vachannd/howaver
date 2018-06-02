__author__ = "Sudheer"

from src import integer_complexity

expected_integer_complexities = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 7, 8, 8, 8, 8, 9, 8, 9, 9, 9, 10, 11,
                                 9, 10, 10, 9, 10, 11, 10, 11, 10, 11, 11, 11, 10, 11, 11, 11, 11,
                                 12, 11, 12, 12, 11, 12, 13, 11, 12, 12, 12, 12, 13, 11, 12, 12,
                                 12, 13, 14, 12, 13, 13, 12, 12, 13, 13, 14, 13, 14, 13, 14, 12,
                                 13, 13, 13, 13, 14, 13, 14, 13,
                                 12, 13, 14, 13, 14, 14, 14, 14, 15, 13, 14, 14, 14, 15, 14, 13, 14, 14, 14, 14]


def verify_first_hundred_complexities():
    actual_integer_complexities = []
    for x in range(1, 101):
        actual_integer_complexities.append(integer_complexity.get_integer_complexity(x))
    i = 0
    while i < 100:
        assert expected_integer_complexities[i] == actual_integer_complexities[i], str(
            expected_integer_complexities[i]) + " " + str(actual_integer_complexities[i]) + " " + str(i + 1)
        i += 1
    assert 1113 == sum(actual_integer_complexities)


def verify_sum_of_first_thousand_complexities():
    actual_integer_complexities = []
    for x in range(1, 1001):
        actual_integer_complexities.append(integer_complexity.get_integer_complexity(x))
    assert 18274 == sum(actual_integer_complexities)


def verify_sum_of_million_complexities():
    """Log this test. It should not take more than 5 seconds. If it does, improve the code."""
    actual_integer_complexities = []
    for x in range(1, 1000001):
        actual_integer_complexities.append(integer_complexity.get_integer_complexity(x))
    assert 39519866 == sum(actual_integer_complexities)


def test_integer_complexity():
    verify_sum_of_million_complexities()
