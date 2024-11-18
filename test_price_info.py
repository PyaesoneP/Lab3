import price_info

def test_total_cost_shopping():
    test_price = 46.75
    result_price = price_info.total_cost_shopping()
    assert(result_price==test_price)
