# Challenge

Implement a Queue using two Stacks

## Feature Tasks

- Create a new classed called pseudo queue.
  - Do not use an existing Queue.
  - Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below).
  - Internally, utilize two `Stack` instances to create and manage the queue.
- Methods:
  - `enqueue`
    - Arguments: value
    - Inserts `value` into the PseudoQueue, using a _first-in, first-out_ approach.
  - `dequeue`
    - Arguments: none
    - Extracts a value from the PseudoQueue, using a _first-in, first-out_ approach.
- NOTE:
  - The `Stack` instances have only `push`, `pop`, and `peek` methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

### Example

PsuedoQueue already has `[10] -> [15] -> [20]`

- Input: `enqueue(5)`
- Output: `[5] -> [10] -> [15] -> [20]`
- `dequeue()`
- Output: `[5] -> [10] -> [15]`

### Approach

If the algorithm is going to use first-in, first-out, its behavior will still be that of a Queue. The difference from this queue to a normal queue is rather than instantiating the Queue with its front and rear attributes set to `None`, it will instead instantiate the Queue with its front and rear attributes set to a new `Stack` instance.

#### Pseudo code

``` #psuedo code for python
class PseudoQueue:
    def __init__(self, front, rear):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self, value):
        # create a variable to instantiate a new node that takes in value
        new_node = Node(value)
        # Make a check to see if the front is empty. if so, change front and rear to both store a new node
        # Since front and rear are both empty stacks, you can use the push() method to create a new node and pass new node into push
        if self.front is None:
            self.front.push(new_node)
            self.rear.push(new_node)
        # If front already has a value, change rear.next to point to the next node and change it to be a new node
        else:
            self.rear = new_node
            self.rear.next_node = self.rear.push(new_node)

    def dequeue(self):
    # Create a temp node to store the front of the queue
    temp = self.front
    self.front = self.front.next
    return temp.value

```

## Algorithm

Walking through my pseudo code, I realize that my code wouldn't be very efficient in utilizing the methods I have available when creating new `Stack` instances. If my front and rear instantiate a new stack, then my enqueue method would need to:

1. Create an enqueue method that takes value
2. Instantiate a new node that takes in value
3. Check if the front has value already (you can use the `peek` method), if it doesn't, use Stack's `push()` method and pass the node into front and rear.
4. Otherwise front has value, and I need to enqueue to the rear of the queue by using rear.push and passing in new_node.next
5. Create a dequeue method that takes no parameters
6. Check if front has value using `front.peek()`, if it does, use `front.pop()` method
