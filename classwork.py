# ------------------- NODE & LINKED LIST CLASSES -------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 3a. Insert after a given node
    def insert_after_node(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if current is None:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # 3b. Insert before a given node
    def insert_before_node(self, next_data, data):
        if self.head is None:
            print("List is empty.")
            return
        # Special case: insert before head
        if self.head.data == next_data:
            self.insert_at_beginning(data)
            return
        prev = None
        current = self.head
        while current and current.data != next_data:
            prev = current
            current = current.next
        if current is None:
            print(f"Node with data {next_data} not found.")
            return
        new_node = Node(data)
        prev.next = new_node
        new_node.next = current

    # 4. Remove a node
    def remove_node(self, target_data):
        if self.head is None:
            print("List is empty.")
            return
        # Special case: target is head
        if self.head.data == target_data:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current and current.data != target_data:
            prev = current
            current = current.next
        if current is None:
            print(f"Node with data {target_data} not found.")
            return
        prev.next = current.next

    # Display the linked list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)



ll = LinkedList()

# Insert at beginning
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.display()  # Expected: [5, 10]

# Insert at end
ll.insert_at_end(20)
ll.insert_at_end(25)
ll.display()  # Expected: [5, 10, 20, 25]

# Insert after node
ll.insert_after_node(10, 15)
ll.display()  # Expected: [5, 10, 15, 20, 25]

# Insert before node
ll.insert_before_node(20, 18)
ll.display()  # Expected: [5, 10, 15, 18, 20, 25]

# Remove a node
ll.remove_node(15)
ll.display()  # Expected: [5, 10, 18, 20, 25]

# Remove head
ll.remove_node(5)
ll.display()  # Expected: [10, 18, 20, 25]

# Remove non-existent node
ll.remove_node(100)  # Node with data 100 not found.