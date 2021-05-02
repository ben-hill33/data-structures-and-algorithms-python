# Stacks and Queues
- [Click here](./stacks_and_queues.py) for code implementation for the challenge below
- [Click here](../../tests/test_stacks_and_queues.py) for unit tests for challenge below
- [Click here](stack_queue/queue.py) for another version of a Queue
- [Click here](stack_queue/stack.py) for another version of a Stack
- [Click here](stack_queue/tower_game.py) for my Towers of Hanoi game using my Stack data structure!!
- [Back to Table of Contents](../README.md)

## Challenge
- Create a **Node class** that has properties for the value stored in the Node, and a pointer to the next node.
- Create a **Stack class** that has a top property. It creates an empty Stack when instantiated.
  - This object should be aware of a default empty value assigned to top when the stack is created.
  - Define a method called **push** which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
  - Define a method called **pop** that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
    - Should raise exception when called on empty stack
  - Define a method called **peek** that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
    - Should raise exception when called on empty stack
  - Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack **is empty**.

- Create a **Queue class** that has a front property. It creates an empty Queue when instantiated.
  - This object should be aware of a default empty value assigned to **front** when the queue is created.
  - Define a method called **enqueue** which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
  - Define a method called **dequeue** that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
    - Should raise exception when called on empty queue
  - Define a method called **peek** that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
    - Should raise exception when called on empty queue
  - Define a method called **isEmpty** that takes no argument, and returns a boolean indicating whether or not the queue is empty.
- Be sure to follow your languages best practices for naming conventions.

### Structure and Testing
1. Can successfully push onto a stack
1. Can successfully push multiple values onto a stack
1. Can successfully pop off the stack
1. Can successfully empty a stack after multiple pops
1. Can successfully peek the next item on the stack
1. Can successfully instantiate an empty stack
1. Calling pop or peek on empty stack raises exception
1. Can successfully enqueue into a queue
1. Can successfully enqueue multiple values into a queue
1. Can successfully dequeue out of a queue the expected value
1. Can successfully peek into a queue, seeing the expected value
1. Can successfully empty a queue after multiple dequeues
1. Can successfully instantiate an empty queue
1. Calling dequeue or peek on empty queue raises exception
