from data_structures.stacks_and_queues.stack_queue.node import Node

class Stack:
  def __init__(self, name):
    """
    Constructor for default values when instantiated
    """
    self.top_item = None
    self.size = 0
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    """
    Adds a node to the top of the stack
    """
    item = Node(value)
    if self.has_space():
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print(f"Adding {item.get_value()} to the stack!")
    else:
      print(f"No room for {item.get_value()}!")

  def pop(self):
    """
    Removes a node from the top of the stack if not empty
    """
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print(f"Popped {item_to_remove.get_value()} off the stack!")
      return item_to_remove.get_value()
    print("Stack is empty!")

  def peek(self):
    """
    Returns the top node's value if not empty
    """
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self) -> bool:
    """
    Helper function to check if there's room in the stack
    """
    return self.limit > self.size

  def is_empty(self) -> bool:
    """
    Helper function to check if stack is empty
    """
    return self.size == 0

  def get_size(self):
    """
    Returns the current size of stack
    """
    return self.size

  def print_items(self):
    pointer = self.top_item
    print_list = []
    while pointer:
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print(f"{print_list} Stack: {self.get_name()}")

  # For tower of hanoi game
  def get_name(self):
    return self.name




# # Defining an empty pizza stack
# pizza_stack = Stack(6)
# # Adding pizzas as they are ready until we have no more room
# pizza_stack.push("pizza #1")
# pizza_stack.push("pizza #2")
# pizza_stack.push("pizza #3")
# pizza_stack.push("pizza #4")
# pizza_stack.push("pizza #5")
# pizza_stack.push("pizza #6")

# # Outputs empty print statement
# pizza_stack.push("pizza #7")

# # Delivering pizzas from the top of the stack down
# print(f"The first pizza to deliver is {pizza_stack.peek()}")
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()

# pizza_stack.pop()