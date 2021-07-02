# Binary search trees:
    # Reference two children at most per tree node.
    # The “left” child of the tree must contain a value lesser than its parent
    # The “right” child of the tree must contain a value greater than its parent.
# Trees are an abstract data type, meaning I can use them in a variety of ways as long as I follow the rules above.

# Strategy:
# 1. Base case: the input list is empty
#    2. Return "No children"
# 3. Recursive step: the input list must be divided into two halves
#   4. Find the middle index of the list
#   5. Store the value located at the middle index
#   6. Make a tree node with a "data" key set to the value
#   7. Assign tree node's "left child" to a recursive call using the left half of the list
#   8. Assign tree node's "right child" to a recursive call using the right half of the list
#   9. Return tree node

def build_bst(my_list):
    # Base Case
    if my_list == []:
        return "No children"
    # Recursive step
    mid_idx = len(my_list) // 2
    mid_value = my_list[mid_idx]
    print(f"Middle index: {mid_idx}")
    print(f"Middel value: {mid_value}")
    # Start building tree
    tree_node = {"data": mid_value}
    tree_node["left_child"] = build_bst(my_list[:mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1:])
    return tree_node

# BIG O: N * logN
# N is the length of the input
# The tree will log N levels deep, as it's unknown how many parent-child relationships it will create
# Each left and right recursive call of N elements are being reduced by one each time (read the length of the list, divide by 2, store the values of the list cut in half), therefore Nth element will multiply and log N levels deep

sorted_list = [12, 13, 14, 15, 16, 17, 18]
bst = build_bst(sorted_list)
