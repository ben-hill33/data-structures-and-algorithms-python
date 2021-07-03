class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class EmptyException(BaseException):
    pass


class Stack:
    def __init__(self, top=None):
        self.top = top

    def is_empty(self) -> bool:
        """
        Returns boolean indicating whether or not the stack is empty
        """
        if self.top is None:
            return True
        else:
            return False

    def push(self, value):
        """
        Adds a new node with value argument to the top of the stack with O(1) runtime

        Args:
            value: Any
        """
        new_node = Node(value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Removes a node from the top of the stack with O(1) runtime.

        Checks is_empty() method to ensure that exception is not raised if stack is empty.
        """
        if self.is_empty():
            raise EmptyException("Stack is empty!")
        temp_node = self.top
        self.top = self.top.next_node
        return temp_node.value

    def peek(self):
        """
        Returns value of the node located at the top of the stack with O(1) runtime.

        Should raise exception when called on empty stack.
        """
        if self.is_empty():
            raise EmptyException("Stack is empty!")
        return self.top.value
