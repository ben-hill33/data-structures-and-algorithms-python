# TreeNode needs a value
class TreeNode:
    def __init__(self, value):
        print('Initializing Groot...')
        self.value = value
        self.children = []

    # can add a node as a child
    def add_child(self, child_node):
        print(f"Adding {child_node.value}")
        # Tells the computer that no node can have more than 2 children
        if len(self.children) == 2:
            print("Nodes can only have 2 children!")
            return
        # Prevents adding a child that already exists
        if child_node in self.children:
            print("Node already exists!")
            return
        self.children.append(child_node)

    # can remove a child
    def remove_child(self, child_node):
        print(f"Removing {child_node.value} from {self.value}")
        self.children = [
            child for child in self.children if child is not child_node]

    # can traverse connected nodes
    def traverse(self):
        print("Traversing...")
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


# have a reference to zero or more other TreeNodes
groot_root = TreeNode("Groot root")
groot_child = TreeNode("I am Groot")
prune_groot = TreeNode("I'm a bad, bad, groot")
groot_three = TreeNode("I am a good Groot")

groot_root.add_child(groot_child)
groot_child.add_child(prune_groot)
prune_groot.add_child(groot_three)

# groot_root.remove_child(prune_groot)
groot_root.traverse()
