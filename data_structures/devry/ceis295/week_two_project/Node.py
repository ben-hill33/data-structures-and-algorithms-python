# Name: Ben Hill
# Date: 5/7/2023

class Node:
    '''
    Node object for DeVry project
    '''
    def __init__(self, initial_data=None):
        self.data = initial_data
        self.next = None

# # Create the linked list
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)

# # Print the memory addresses and values of each node
# curr = head
# while curr is not None:
#     print(f"Node at memory address {id(curr)} has value {curr.data}")
#     curr = curr.next
