from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    item = Node(value)
    if self.has_space():
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print(f"Adding {item.get_value()} to the stack!")
    else:
      print(f"No room for {item.get_value()}!")

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print(f"Completed {item_to_remove.get_value()}")
      return item_to_remove.get_value()
    print("Stack is empty!")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self) -> bool:
    return self.size == 0

# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have no more room
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Outputs empty print statement
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print(f"The first pizza to deliver is {pizza_stack.peek()}")
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

pizza_stack.pop()