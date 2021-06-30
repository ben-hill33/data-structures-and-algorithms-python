from algorithms.recursion.call_stack import sum_to_one


def test_n_value_two_equals_one():
    expected = (1, [{'n_value': 2}])
    actual = sum_to_one(2)
    assert actual == expected
