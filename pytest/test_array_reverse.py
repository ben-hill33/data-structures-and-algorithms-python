from challenges.array_reverse import array_reverse


def test_reverse_array():
    in_order = ["Claire", "Aubrey", "Evan"]
    expected = in_order[::-1]
    actual = array_reverse.reverse_array(in_order)
    assert actual == expected


def test_reverse_array_add():
    in_order = ["Claire", "Aubrey", "Evan", "Delta"]
    expected = in_order[::-1]
    actual = array_reverse.reverse_array(in_order)
    assert actual == expected
