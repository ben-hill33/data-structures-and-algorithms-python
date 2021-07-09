from data_structures.linked_list.ll_three import Node, LL_three


def test_node_instance_takes_value():
    node = Node(1)
    expected = 1
    actual = node.value
    assert actual == expected


def test_nodes_next_value_is_none():
    node = Node(0)
    expected = None
    actual = node.next_node
    assert actual == expected


def test_ll_instantiates_empty_ll():
    ll = LL_three()
    expected = None
    actual = ll.head
    assert actual == expected


def test_insert_to_head_of_ll():
    ll = LL_three()
    ll.insert_head(1)
    expected = 1
    actual = ll.head.value
    assert actual == expected


def test_can_insert_multiple():
    ll = LL_three()
    ll.insert_head(1)
    ll.insert_head(2)
    expected = 2
    actual = ll.head.value
    assert actual == expected
