# BST implementation

## Methods:
- _Insertion_: 
  - If a new value is less than the root node's value, we want to insert it to its left or right subtree.
  - If a new value is less than the root node's value, insert new _BST()_ to its left subtree.
  - If a new value is greater than the root node’s value, insert new _BST()_ to its right subtree.
  - If left or right child doesn't exist, create a new one. If left or right child already exists, call insert() recursively on the current node's left or right child to insert further down.

- _Pseudo code_:

If the new value is less than the root node's value
  If a left child node does not exist
    Create new BST with new value and updated depth and assign it to the left pointer
  Else
    Recursively call insert() on the left child node
Else
  If a right child node does not exist
    Create a new BST with new value and updated depth and assign it to the right pointer
  Else
    Recursively call insert() on the right child node

