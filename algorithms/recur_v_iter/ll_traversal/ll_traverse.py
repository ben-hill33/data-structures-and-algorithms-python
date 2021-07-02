from algorithms.recur_v_iter.ll_traversal.linked_list import LinkedList

my_list = LinkedList()

my_list.insert_beginning("Node 1")
my_list.insert_beginning("Node 2")
my_list.insert_beginning("Node 3")
my_list.insert_beginning("Node 4")

find_node = my_list.find_node_iteratively("Node 2")
print(find_node.value)

# RECURSIVE TRAVERSAL
# Will need two parameters: value(value of the Node that is being searched for), current_node(current node in the ll, during each recursive call, the method will pass the next node as this argument)

# Base case should only return a value if:
# the method finds a node with the matching value, in which case it should return the node
# the method reaches the end of teh list without finding a node with the matchinig value, return None

find_node_recur = my_list.find_node_recursively("Node 4")
print(find_node_recur.value)
