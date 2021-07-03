from data_structures.stacks_and_queues.stack_two import Stack, EmptyException

import pytest

def test_stack_is_empty():
    stack = Stack()
    expected = True
    actual = stack.is_empty()
    assert actual == expected


def test_hasattr_method_returns_false_when_given_attr_that_doesnt_exist():
    stack = Stack()
    has_method = hasattr(stack, 'fake_method')
    assert has_method is False


def test_push_method_exists():
    stack = Stack()
    has_method = hasattr(stack, 'push')
    assert has_method is True


def test_push_adds_node_to_top_of_stack():
    stack = Stack()
    stack.push("Test")
    expected = "Test"
    actual = stack.top.value
    assert actual == expected


def test_top_is_not_none_after_pushing():
    stack = Stack()
    stack.push(1)
    assert stack.top.value is not None


def test_push_adds_multiple_nodes_to_top_of_stack():
    stack = Stack()
    stack.push("One")
    stack.push("Two")
    stack.push("Three")
    expected = "Three"
    actual = stack.top.value
    assert actual == expected


def test_pop_method_exists():
    stack = Stack()
    has_method = hasattr(stack, 'pop')
    assert has_method is True


def test_pop_raises_empty_exception_if_stack_is_empty():
    stack = Stack()
    with pytest.raises(EmptyException) as empty:
        stack.pop()

    assert str(empty.value) == "Stack is empty!"


def test_pop_one():
    stack = Stack()
    stack.push(1)
    stack.pop()
    expected = True
    actual = stack.is_empty()
    assert actual == expected


def test_is_empty_returns_false_if_stack_has_value():
    stack = Stack()
    stack.push(1)
    expected = False
    actual = stack.is_empty()
    assert actual == expected


def test_stack_empties_after_multiple_pops():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    expected = True
    actual = stack.is_empty()
    assert actual == expected


def test_peek_raises_empty_exception_if_stack_is_empty():
    stack = Stack()
    with pytest.raises(EmptyException) as empty:
        stack.peek()

    assert str(empty.value) == "Stack is empty!"


def test_peek_returns_top_value():
    stack = Stack()
    stack.push(1)
    expected = 1
    actual = stack.peek()
    assert expected == actual
