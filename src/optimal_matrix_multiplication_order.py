__author__ = "Sudheer"


def get_operations(order1, order2):
    return order1[0] * order1[1] * order2[1]


def get_cost(orders, map):
    try:
        return map[tuple(orders)]
    except KeyError as e:
        pass


def set_cost(orders, map, value):
    map[tuple(orders)] = value


def get_total_operations(orders, cost_map):
    if len(orders) <= 1:
        return 0
    elif len(orders) == 2:
        if get_cost(orders, cost_map) is None:
            set_cost(orders, cost_map, get_operations(orders[0], orders[1]))
        return get_cost(orders, cost_map)
    index = 1
    for x in orders[:-1]:
        left_half = orders[:index]
        right_half = orders[index:]
        left_half_cost = get_total_operations(left_half, cost_map)
        right_half_cost = get_total_operations(right_half, cost_map)
        total_operation_cost = left_half_cost + right_half_cost
        final_product_cost = get_operations(
            (left_half[0][0], left_half[-1][1]), (right_half[0][0], right_half[-1][1])
        )
        total_operation_cost = total_operation_cost + final_product_cost
        current_optimal_cost = get_cost(orders, cost_map)
        if current_optimal_cost is None or total_operation_cost < current_optimal_cost:
            set_cost(orders, cost_map, total_operation_cost)
        index += 1
    return get_cost(orders, cost_map)


def optimal_matrix_multiplication_operations(order_list: list) -> int:
    multiplication_operation_cost_map = {}
    matrix_orders = list(zip(order_list, order_list[1:]))
    return get_total_operations(matrix_orders, multiplication_operation_cost_map)
