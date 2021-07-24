from data_structures.tree.tree_three import (
    EmptyException,
    Node
)


def test_node_exists():
    node = Node(0)
    assert node


def test_node_has_left_child():
    node = Node(0)
    assert node.left_child is None


def test_node_has_right_child():
    node = Node(0)
    assert node.right_child is None


# Can successfully instantiate an empty tree
def test_instantiate_empty_tree():
    pass


# Can successfully instantiate a tree with a single root node
def test_instantiate_tree_with_single_root_node():
    pass


# Can successfully add a left child and right child to a single root node
def test_adding_a_left_and_right_child_to_single_root():
    pass


# Can successfully return a collection from a preorder traversal
def test_returns_collection_preorder():
    pass


# Can successfully return a collection from an inorder traversal
def test_returns_collection_in_order():
    pass


# Can successfully return a collection from a postorder traversal
def test_return_collection_postorder():
    pass
