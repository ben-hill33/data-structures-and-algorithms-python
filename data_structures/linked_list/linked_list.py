class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(ValueError):
    pass


class LinkedList:
    """
    Singly Linked List
    """
    def __init__(self, head=None, values=None):
        self.head = head

        if values:
            for value in reversed(values):
                self.insert(value)

    def __str__(self):
        """
        Gives stringy format to list
        """
        output = ""
        current = self.head
        while current:
            output += f"{{ {current} }} -> "
            current = current.next
        return output + "NONE"

    def insert(self, value):
        """
        Adds value to head, or beginning, of list
        """
        self.head = Node(value, self.head)

    def includes(self, value):
        """
        returns True/False if value found in list
        """
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        """
        Adds value to end of list
        """
        node = Node(value)

        if not self.head:
            self.head = node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = node

    def insert_before(self, value, new_val):
        """
        Inserts new value before the given value
        """
        current = self.head

        if current and current.value == value:
            self.head = Node(new_val, self.head)
            return
        
        while current and current.next:
            if current.next.value == value:
                node = Node(new_val, current.next)
                current.next = node
                return
            current = current.next
        raise TargetError(f"{value} not in list")

    def insert_after(self, value, new_val):
        """
        Inserts new value after the given value
        """
        current = self.head
        while current:
            if current.value == value:
                node = Node(new_val, current.next)
                current.next = node
            current = current.next
        raise TargetError(f"{value} not in list")
        # return self.head

    def kth_number(self, k):
        current = self.head

        previous = None

        counter = 0
        while current:
            current = current.next
            if previous:
                previous = previous.next
            elif counter == k:
                previous = self.head
            else:
                counter += 1

        if not previous:
            raise TargetError(f"k is not in Linked List!")
        return previous.value
