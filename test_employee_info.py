import employee_info

def test_get_employees_by_age_range():
    result = []
    test_employees = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
        ]
    input_lower_age = 24
    input_upper_age = 40
    result = employee_info.get_employees_by_age_range(input_lower_age,input_upper_age)
    assert(result==test_employees)

def test_calculate_average_salary():
    test = 60166.667
    result = employee_info.calculate_average_salary()
    assert(result==test)
