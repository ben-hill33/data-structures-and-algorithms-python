class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class EmptyException(BaseException):
    pass


class LL_three:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        """
        Adds a new node with that value to the head of the list with an O(1) runtime.
        """
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def includes(self, value):
        """
        Indicates whether or not a value exists as a Node's value somewhere within the list.

        Returns: Boolean
        """
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node

    def to_string(self):
        """
        Returns a string representing all the values in the Linked List
        """
