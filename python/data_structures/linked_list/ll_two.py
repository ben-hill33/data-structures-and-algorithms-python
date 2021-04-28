class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def __str__(self):
    """
    Turns output into a human readable string list

    Returns:
        string: {HEAD} -> {NODE} -> NONE
    """
    output = ""
    current = self.head_node
    while current:
      if current.value != None:
        output += f"{{ {current.value} }} -> "
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

  def add_node_beginning(self, new_value):
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

    if self.head_node:
      new_node.next = self.head_node
    self.head_node = new_node


ll = LinkedList(5)
print(ll)
ll.add_node_beginning(4)
print(ll)