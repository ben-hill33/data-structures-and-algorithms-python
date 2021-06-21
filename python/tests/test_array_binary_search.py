from challenges.array_binary_search.arr_bin_search_two import binary_search


def test_one():
    actual = binary_search(["apples"], "apples")
    expected = 0
    assert actual == expected


def test_three_keys_in_mid():
    actual = binary_search(["a", "b", "c"], "b")
    expected = 1
    assert actual == expected
