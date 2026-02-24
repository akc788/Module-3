class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list
        """
        new_node = ListNode(value)
        if not self._tail:  # empty list
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        """
        Remove the last element of the list and return its data.
        Returns None if the list is empty.
        """
        # Case 1: empty list
        if not self._head:
            return None

        # Case 2: only one node
        if self._head == self._tail:
            val = self._head.data
            del self._head
            self._head = None
            self._tail = None
            self._size = 0
            return val

        # Case 3: more than one node
        current_node = self._head
        while current_node.next != self._tail:
            current_node = current_node.next

        val = self._tail.data
        del self._tail
        self._tail = current_node
        self._tail.next = None
        self._size -= 1
        return val