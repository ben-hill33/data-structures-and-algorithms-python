class Node:
    """
    Node object with properties for the value stored in the Node, and a pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next_node = None


class EmptyException(BaseException):
    pass


class Stack:
    """
    Stack object with top property. It creates an empty Stack when instantiated.
    """
    def __init__(self, top=None):
        self.top = top

    def __str__(self):
        output = ''
        current = self.top
        while current is not None:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output + '\nNONE\n'

    def is_empty(self) -> bool:
        """
        Returns boolean indicating whether or not the stack is empty
        """
        if self.top is None:
            return True
        else:
            return False

    def push(self, value):
        """
        Adds a new node with value argument to the top of the stack with O(1) runtime

        Args:
            value: Any
        """
        new_node = Node(value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Removes a node from the top of the stack with O(1) runtime.

        Checks is_empty() method to ensure that exception is not raised if stack is empty.
        """
        if self.is_empty():
            raise EmptyException("Stack is empty!")
        temp_node = self.top
        self.top = self.top.next_node
        return temp_node.value

    def peek(self):
        """
        Returns value of the node located at the top of the stack with O(1) runtime.

        Should raise exception when called on empty stack.
        """
        if self.is_empty():
            raise EmptyException("Stack is empty!")
        return self.top.value


class Queue:
    """
    Queue object with front and rear properties. It creates an empty Queue when instantiated.
    """
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def __str__(self):
        output = ''
        current = self.front
        while current:
            output += f'{{ {current.value} }} -> '
            current = current.next_node
        return output + 'NONE\n'

    def is_empty(self) -> bool:
        """
        Returns boolean indicating whether or not Queue is empty.

        Returns True if front's value is None, otherwise returns False.
        """
        if self.front is None:
            return True
        else:
            return False


    def enqueue(self, value):
        """
        Adds a new node with that value to back of the queue with O(1) runtime. Next node points to rear.

        Args:
            value (new Node): Instantiates a new Node to the rear of the queue.
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Removes a node from the front of the Queue with O(1) runtime.

        Should raise exception when called on empty Queue.
        """
        if self.is_empty():
            raise EmptyException("Queue is empty!")
        temp_node = self.front
        self.front = self.front.next_node
        return temp_node.value

    def peek(self):
        """
        Returns value of the node located at the front of the Queue.

        Should raise exception when called on empty Queue.
        """
        if self.is_empty():
            raise EmptyException("Queue is empty!")
        return self.front.value

new_node = Node(1)

# stack = Stack()
# print(stack)

# stack.push(2)
# stack.push(1)
# stack.push('TOP')
# print(stack)

# stack.pop()
# stack.pop()
# print(stack)

queue = Queue()
print(queue)


queue.enqueue('FRONT')
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue('BACK')
print(queue)

queue.dequeue()
print(queue)

print(queue.peek())
