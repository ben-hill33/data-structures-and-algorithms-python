# Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# Create a BinaryTree class
class BinaryTree:
  def __init__(self, value):
    self.root = Node(value)
    self.depth = 1

  def size(self):
    return self.depth

# Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which / returns an array of the values / , ordered appropriately.
  def pre_order(self):
    output = []

    def traverse(child_node):
      # root node value
      print(f'Value={output.value}')
      # if left child exists, go left
      if child_node.left is not None:
        traverse(child_node.left)
      # if right child exists, go right
      if child_node.right is not None:
        traverse(child_node.right)

    traverse(self.root)
    return output

  def in_order(self):
    output = []

    def traverse(child_node):
      if child_node.left is not None:
        traverse(child_node.left)
      print(f'Value={output.value}')
      if child_node.right is not None:
        traverse(child_node.right)

    traverse(self.root)
    return output

  def post_order(self):
    output = []

    def traverse(child_node):
      if child_node.left is not None:
        traverse(child_node.left)
      if child_node.right is not None:
        traverse(child_node.right)
      print(f'Value={output.value}')

    traverse(self.root)
    return output



# Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
BinaryTree()
