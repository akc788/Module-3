class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = value

    def append(self, value):
        new_node = ListNode(value, next=None, prev=self._tail)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        if not self._size:
            return None
        node_to_remove = self._tail
        previous_node = node_to_remove.prev
        if node_to_remove == self._head:
            self._head = self._tail = None
        else:
            previous_node.next = None
            self._tail = previous_node
        self._size -= 1
        value = node_to_remove.data
        del node_to_remove
        return value

    def contains(self, value):
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        current_node = self._head
        while current_node:
            next_node = current_node.next
            del current_node
            current_node = next_node
        self._head = self._tail = None
        self._size = 0

    def insert(self, index, value):
        """
        Insert a new node with value at the given index
        """
        if index < 0 or index > self._size:
            raise ValueError('Index out of bounds')

        # Insert at the end (same as append)
        if index == self._size:
            self.append(value)
            return

        # Move to the node currently at the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # Node before current
        previous_node = current_node.prev

        # Create new node
        new_node = ListNode(value, next=current_node, prev=previous_node)

        # Update previous node if exists
        if previous_node:
            previous_node.next = new_node
        else:
            # Inserting at head
            self._head = new_node

        # Update current node's prev
        current_node.prev = new_node

        # Increase size
        self._size += 1