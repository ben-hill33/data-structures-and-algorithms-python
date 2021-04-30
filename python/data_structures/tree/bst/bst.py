class BST:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

  def insert(self, value):
    """If a new value is less than the root node's value, insert it to its left subtree.

    If a new value is greater than the root node’s value, insert it to its right subtree.

    If left or right child doesn't exist, create a new one. If left or right child already exists, call insert() recursively on the current node's left or right child to insert further down.
    """
    if value < self.value:
      if self.left is None:
        self.left = BST(value, self.depth + 1)
        print(f"Tree node {value} added to the left of {self.value} at depth {self.depth + 1}")
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BST(value, self.depth + 1)
        print(f"Tree node {value} added to the right of {self.value} at depth {self.depth + 1}")
      else:
        self.right.insert(value)

  def get_node_by_value(self, value):
    """If target value is the same as the current node value, return the current node

    Else if there is a left child node and target value is less than the root node's value

    """
    #base case
    if (self.value == value):
      return self
    elif ((self.left is not None) and (value < self.value)):
      return self.left.get_node_by_value(value)
    elif ((self.right is not None) and (value >= self.value)):
      return self.right.get_node_by_value(value)
    else:
      return None



root = BST(100)
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

print(root.get_node_by_value(75).value, "is in BST")
print(root.get_node_by_value(55))

