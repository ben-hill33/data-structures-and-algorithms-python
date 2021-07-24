# Custom node is empty exception
class EmptyException(BaseException):
    pass


class Node:
    """
    Node class has properties for the value stored in the node, the left child node, and the right child node.
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    """Binary Tree class with depth first traversal methods.
    """
    def __init__(self):
        self.root_node = root_node

    def pre_order_traversal(self):
        """root -> left -> right
        """
        if self.root_node:
            print(self.root_node.value),
            self.pre_order_traversal(self.root_node.left_child)
            self.pre_order_traversal(self.root_node.right_child)


    def in_order_traversal(self):
        """left -> root -> right
        """
        pass

    def post_order_traversal(self):
        """
        Returns an array of the values, ordered appropriately.

        left -> right -> root
        """
        pass

    def is_empty(self) -> bool:
        """Returns boolean indicating whether the tree is empty.

        Returns:
            bool: If tree is empty will return True, otherwise False.
        """


class BinarySearchTree(BinaryTree):
    def add(self, value):
        """Adds a new node with the value in the correct location in the binary search tree.

        Args:
            value
        Returns:
            nothing
        """
        pass

    def contains(self, value):
        """Returns boolean indicating whether or not the value is in the tree at least once.

        Args:
            value (Node): Returns True if a value is found in the tree, otherwise returns False.
        """

tree = BinaryTree("ROOT")
print(tree.root_node.value)
print(tree.root_node.left_child)
print(tree.root_node.right_child)

