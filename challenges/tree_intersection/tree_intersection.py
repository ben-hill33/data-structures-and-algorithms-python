class Node:
    ''' stores binary tree node '''

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def tree_intersection(bt_one, bt_two):
    if bt_one is None and bt_two is None:
      return True

    # if both trees are not empty and the value of their root matches, recur for their left and right subtree
    return (bt_one and bt_two) and \
      (bt_one.key == bt_two.key) and \
        tree_intersection(bt_one.left, bt_two.left) and \
          tree_intersection(bt_one.right, bt_two.right)

