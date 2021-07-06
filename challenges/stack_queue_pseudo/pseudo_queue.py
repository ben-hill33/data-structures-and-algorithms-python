from data_structures.stacks_and_queues.stack_two import Stack, Node


class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self, value):
        new_node = Node(value)
        if self.front.top is None and self.rear.top is None:
            self.front.push(value)
            self.rear.push(value)
        else:
            self.rear = new_node
            self.rear.push(new_node.value)


    def dequeue(self):

        return self.front.pop()


pseudo = PseudoQueue()
pseudo.enqueue(1)
pseudo.enqueue(2)
pseudo.enqueue(3)
pseudo.enqueue(4)
# print(pseudo.front.peek())
print(pseudo.rear.peek())
pseudo.dequeue()
print(pseudo.front.peek())
