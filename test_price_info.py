import price_info

def test_total_cost_shopping():
    test_price = 46.75
    result_price = price_info.total_cost_shopping()
    assert(result_price==test_price)

def test_cost_of_fruit():
    test_cost = 12.0
    input_fruit = 'apple'
    input_quantity = 10
    result_cost = price_info.cost_of_fruits(input_fruit, input_quantity)
    assert(result_cost==test_cost)