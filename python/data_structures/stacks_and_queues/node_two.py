# create a node class with two properties, value for the Node and pointer to next node
class Node:
  # the node's default value needs to be None
  def __init__(self, value, node=None):
    self.value = value
    self.node = node
