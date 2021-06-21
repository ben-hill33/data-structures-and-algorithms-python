from queue_one import Queue
from ll_two import LinkedList

def merge_lists(ll_one, ll_two):
  node = Queue()
  temp = node
  while temp:
    if ll_one is None:
      temp.next = ll_two
      break
    if ll_two is None:
      temp.next = ll_one
      break
    if ll_one.value <= ll_two.value:
      temp.next = ll_one
      ll_one = ll_one.next
    else:
      temp.next = ll_two
      ll_two = ll_two.next
    temp = temp.next
  return node.next
  
  # zip_list = Queue(10)
  # head_one = LinkedList(ll_one)
  # head_two = LinkedList(ll_2)
  # if head_one.head_node:
  #   zip_list.enqueue(head_one).item_to_add
  #   head_two.head_node = head_one.head_node.next

  #   zip_list.enqueue(head_two)

    # head_one.head_node(ll_2)
  # if head_two:
  #   head_two.set_next_node(ll_1)

  # return zip_list

ll_1 = LinkedList()
ll_2 = LinkedList()

ll_1.add_node(1)
ll_1.add_node(3)
ll_1.add_node(5)
print(ll_1)
ll_2.add_node(2)
ll_2.add_node(4)
ll_2.add_node(6)
print(ll_2)

ll_1.head_node = merge_lists(ll_1.head_node, ll_2.head_node)
ll_1.print_list()
# merged_list.enqueue(ll_1)
# merged_list.enqueue(ll_2)
# print(f"Peeking at...{merged_list.peek()}")
# print(merged_list.get_size())
