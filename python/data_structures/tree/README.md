# Trees Implementation
## Author: Ben Hill

- [Click here](./tree.py) for Binary Tree and Binary Search Tree with no built in methods that solves the challenge below
- [Click here](tree_two.py) for Binary Tree with built in methods
- [Click here](adventure.py) for an adventure game using a Binary Tree (courtesy of codecademy)
### Challenge

- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Create a BinaryTree class
  - Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
- Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

- Create a BinarySearchTree class
- Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
- Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

Write tests to prove the following functionality:
- [Click here](../../tests/test_tree.py) for tests (tests are only for no built in methods version)

- Can successfully instantiate an empty tree
- Can successfully instantiate a tree with a single root node
- Can successfully add a left child and right child to a single root node
- Can successfully return a collection from a preorder traversal
- Can successfully return a collection from an inorder traversal
- Can successfully return a collection from a postorder traversal
- Ensure your tests are passing before you submit your solution.

#### Stretch Goal
- Create a new branch called k-ary-tree, and, using the resources available to you online, 
  - implement a k-ary tree, where each node can have any number of children.