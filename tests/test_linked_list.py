from data_structures.linked_list.linked_list import LinkedList, TargetError


def test_instantiate_empy_ll():
    tester = LinkedList()
    assert tester.head == None


def test_insert_into_head_of_ll():
    tester = LinkedList()
    tester.insert(10)
    assert tester.head.value == 10


def test_insert_multiple_nodes_at_head_of_ll():
    tester = LinkedList()
    tester.insert(10)
    tester.insert(9)
    assert tester.head.next.value == 10


def test_insert_two_items_fail():
    tester = LinkedList()
    tester.insert(10)
    tester.insert(9)
    assert tester.head.next.value != 9


def test_includes_two_pass():
    tester = LinkedList()
    tester.insert(2)
    actual = tester.includes(2)
    assert actual == True


def test_includes_two_fail():
    tester = LinkedList()
    tester.insert(2)
    actual = tester.includes(3)
    assert actual == False


def test_includes_two_three_pass():
    tester = LinkedList()
    tester.insert(2)
    tester.insert(3)
    actual = tester.includes(2)
    actual = tester.includes(3)
    assert actual == True


def test_includes_two_three_fail():
    tester = LinkedList()
    tester.insert(2)
    tester.insert(3)
    actual = tester.includes(8)
    actual = tester.includes(7)
    assert actual == False


def test_insert_string():
    tester = LinkedList()
    tester.insert('String')
    assert tester.head.value == 'String'


def test_can_append():
    tester = LinkedList()
    tester.append(1)
    tester.append(2)
    assert tester.head.next.value == 2


def test_cannot_append():
    tester = LinkedList()
    tester.append(1)
    tester.append(3)
    assert tester.head.next.value != 2


def test_can_insert_before_middle():
    tester = LinkedList()
    tester.insert(4)
    tester.insert(3)
    tester.insert(2)
    tester.insert(1)
    tester.insert_before(3, "Middle")
    assert tester


def test_can_insert_before_first():
    tester = LinkedList()
    tester.insert(4)
    tester.insert(3)
    tester.insert(2)
    tester.insert(1)
    tester.insert_before(1, "Before first")
    assert tester


# Where k is greater than the length of the linked list

# Where k and the length of the list are the same

# Where k is not a positive integer

# Where the linked list is of a size 1

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
