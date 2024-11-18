import Lab2.bmi as bmi
def test_bmi_underweight():
    input_weight = 40
    input_height = 1.73
    test_val = -1
    result_val = bmi.calculate_bmi(input_height, input_weight)
    assert(result_val == test_val)

def test_bmi_normalweight():
    input_weight = 50
    input_height = 1.5
    test_val = 0
    result_val = bmi.calculate_bmi(input_height, input_weight)
    assert(result_val == test_val)

def test_bmi_overweight():
    input_weight = 70
    input_height = 1.4
    test_val = 1
    result_val = bmi.calculate_bmi(input_height, input_weight)
    assert(result_val == test_val)

