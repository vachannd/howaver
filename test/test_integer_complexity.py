__author__ = "Sudheer"

from random_problems import integer_complexity

actual_integer_complexities = []
expected_integer_complexities = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 7, 8, 8, 8, 8, 9, 8, 9, 9, 9, 10, 11,
                                 9, 10, 10, 9, 10, 11, 10, 11, 10, 11, 11, 11, 10, 11, 11, 11, 11,
                                 12, 11, 12, 12, 11, 12, 13, 11, 12, 12, 12, 12, 13, 11, 12, 12,
                                 12, 13, 14, 12, 13, 13, 12, 12, 13, 13, 14, 13, 14, 13, 14, 12,
                                 13, 13, 13, 13, 14, 13, 14, 13,
                                 12, 13, 14, 13, 14, 14, 14, 14, 15, 13, 14, 14, 14, 15, 14, 13, 14, 14, 14, 14]

for x in range(1, 101):
    actual_integer_complexities.append(integer_complexity.get_integer_complexity(x))


def test_integer_complexity():
    i = 0
    while i < 100:
        assert expected_integer_complexities[i] == actual_integer_complexities[i], str(
            expected_integer_complexities[i]) + " " + str(actual_integer_complexities[i]) + " " + str(i)
        i += 1
    # assert expected_integer_complexities == actual_integer_complexities


def test_sum_of_integer_complexities():
    assert 1113 == sum(actual_integer_complexities)
