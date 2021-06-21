from ..bt import BinaryTree, Node

# Create a BinarySearchTree class
class BST(BinaryTree):
  def __init__(self, value):
    self.root = Node(value)
    self.depth = 1

# Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
  def add(self, value):
    self.depth += 1
    new_node = Node(value)
    
    def search_tree(node):
      if value < node.value:
        if node.left is None:
          node.left = new_node
          print(f"Tree node {value} added to the left of {self.value} at depth {self.depth}")
        else:
          search_tree(node.left)
      else:
        if node.right is None:
          node.right = new_node
          print(f"Tree node {value} added to the left of {self.value} at depth {self.depth}")
        else:
          search_tree(node.right)
    
    search_tree(self.root)

# Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
  def contains(self, value):
    current_node = self.root

    while current_node:
      if value == current_node.value:
        return True
      elif value < current_node.value:
        current_node = current_node.left
      else:
        current_node = current_node.right
    return False