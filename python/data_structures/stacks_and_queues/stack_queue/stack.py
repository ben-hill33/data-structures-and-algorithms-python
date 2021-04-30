# create a node class with two properties, value for the Node and pointer to next node
class Node:
  # the node's default value needs to be None
  def __init__(self, value, node=None):
    self.value = value
    self.node = node

# create a stack class with a top property, it creates an empty stack when instantiated
# Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
# should be aware of a default empty value assigned to top when stack is created
# define a method called push / which takes any value as an argument and adds a new node with that value to the top of the stack with O(1) time performance
# Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value. Should raise exception when called on empty stack
# Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack. Should raise exception when called on empty stack
