from challenges.ll_zip.ll_zip import merge_lists
from data_structures.linked_list.linked_list import LinkedList


def test_insert():
    tester = LinkedList()
    tester.insert(10)
    assert tester.head.value == 10


def test_insert_two_items():
    tester = LinkedList()
    tester.insert(10)
    tester.insert(9)
    assert tester.head.next.value == 10


def test_return_list_one():
    tester = LinkedList()
    test_list = [1, 2, 3]
    tester.insert(test_list[2])
    tester.insert(test_list[1])
    tester.insert(test_list[0])
    expected = '{ 1 } -> { 2 } -> { 3 } -> NONE'
    actual = str(tester)
    assert actual == expected


def test_return_merged():
    test_ll_1 = LinkedList()
    test_ll_2 = LinkedList()
    test_list_one = [1, 3, 5]
    test_list_two = [2, 4, 6]
    test_ll_1.insert(test_list_one[2])
    test_ll_1.insert(test_list_one[1])
    test_ll_1.insert(test_list_one[0])
    test_ll_2.insert(test_list_two[2])
    test_ll_2.insert(test_list_two[1])
    test_ll_2.insert(test_list_two[0])
    test_merge = merge_lists(test_ll_1, test_ll_2)
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NONE'
    actual = str(test_merge)
    assert actual == expected
