class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head_node = None

  # def __str__(self):
  #   """
  #   Turns output into a human readable string list

  #   Returns:
  #       string: {HEAD} -> {NODE} -> NONE
  #   """
  #   output = ""
  #   current = self.head_node
  #   while current:
  #     if current.value != None:
  #       output += f"{{ {current.value} }} -> "
  #     current = current.next
  #   return output + "{ None }"

  def print_list(self):
    output = ""
    current = self.head_node
    while current:
      output += f"{{ {current.value} }} -> "
      print(current.value, end=" -> ")
      current = current.next
    return output + "{ None }"

  def includes(self, value):
    """
    Checks whether Linked List includes a specific value

    Big O
    Time: O(n) Worst case, the node will be the very last node in the linked list
    Space: O(n) No additional space being used than what is already given with the linked list input 

    Args:
        value ([input]): [integer value]

    Returns:
        [output]: [boolean]
    """
    current = self.head_node
    while current:
      if current.value == value:
        return True
      current = current.next
    return False

  def add_node(self, new_value):
    """
    Adds a node to the linked list at the head node

    Big O
    Time: O(1)
    Space: O(1)
    Takes the same amount of time to add a new node to the beginning of the list, and no additional resources are being used

    Args:
        new_node (input value to add ie(4))
    """
    new_node = Node(new_value)

    if self.head_node is None:
      self.head_node = new_node
      return
    
    last = self.head_node
    while last.next:
      last = last.next
    last.next = new_node



# ll = LinkedList(5)
# print(ll)
# ll.add_node(4)
# print(ll)