__author__ = "Sudheer"
from src import between_two_sets


def test_brute_force():
    assert 3 == between_two_sets.get_inbetween_factor_count_brute_force(
        [2, 4], [16, 32, 96]
    )
    assert 0 == between_two_sets.get_inbetween_factor_count_brute_force(
        [100, 99, 98, 97, 96, 95, 94, 93, 92, 91], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    assert 1 == between_two_sets.get_inbetween_factor_count_brute_force(
        [2], [20, 30, 12]
    )
    assert 2 == between_two_sets.get_inbetween_factor_count_brute_force(
        [3, 9, 6], [36, 72]
    )


def test_lcm_gcd():
    assert 3 == between_two_sets.get_inbetween_factor_count_lcm_gcd(
        [2, 4], [16, 32, 96]
    )
    assert 0 == between_two_sets.get_inbetween_factor_count_lcm_gcd(
        [100, 99, 98, 97, 96, 95, 94, 93, 92, 91], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    assert 1 == between_two_sets.get_inbetween_factor_count_lcm_gcd([2], [20, 30, 12])
    assert 2 == between_two_sets.get_inbetween_factor_count_lcm_gcd([3, 9, 6], [36, 72])


def test_optimal():
    assert 3 == between_two_sets.get_inbetween_factor_count_optimal(
        [2, 4], [16, 32, 96]
    )
    assert 0 == between_two_sets.get_inbetween_factor_count_optimal(
        [100, 99, 98, 97, 96, 95, 94, 93, 92, 91], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    assert 1 == between_two_sets.get_inbetween_factor_count_optimal([2], [20, 30, 12])
    assert 2 == between_two_sets.get_inbetween_factor_count_optimal([3, 9, 6], [36, 72])
