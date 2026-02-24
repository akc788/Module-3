class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list
        """
        node = ListNode(value)
        if not self._head:
            self._head = node
        else:
            current_node = self._head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        """
        Remove the last element of the list and return its data.
        Returns None if the list is empty.
        """
        # Case 1: Empty list
        if not self._head:
            return None

        # Case 2: Only one node
        if not self._head.next:
            val = self._head.data
            del self._head
            self._head = None
            return val

        # Case 3: More than one node
        current_node = self._head
        while current_node.next.next:  # stop at second-to-last node
            current_node = current_node.next

        val = current_node.next.data
        del current_node.next
        current_node.next = None
        return val