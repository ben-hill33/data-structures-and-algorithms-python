from algorithms.quick_sort.quick_sort import quick_sort


def test_sort_random():
    arr = [8, 4, 23, 42, 16, 15]
    quick_sort(arr)
    actual = arr
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_in_reverse():
    arr = [20, 18, 12, 8, 5, -2]
    quick_sort(arr)
    actual = arr
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_duplicate_elements():
    arr = [5, 12, 7, 5, 5, 7]
    quick_sort(arr)
    actual = arr
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted():
    arr = [2, 3, 5, 7, 13, 11]
    quick_sort(arr)
    actual = arr
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
