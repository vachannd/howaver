from optimal_matrix_multiplication_order import *

def test_optimal_matrix_multiplication_order():
    assert 4500 == get_optimal_matrix_multiplication_operations([10, 30, 5, 60])
    assert 6000 == get_optimal_matrix_multiplication_operations([10, 20, 30])
    assert 26000 == get_optimal_matrix_multiplication_operations([40, 20, 30, 10, 30])
    assert 30000 == get_optimal_matrix_multiplication_operations([10, 20, 30, 40, 30])