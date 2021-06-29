from data_structures.linked_list.node import Node


class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node

  def print_list(self):
    output = ""
    current = self.head_node
    while current:
      output += f"{{ {current.value} }} -> "
      print(current.value, end=" -> ")
      current = current.next_node
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
      current = current.next_node
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
    while last.next_node:
      last = last.next_node
    last.next_node = new_node

ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node("Four")
