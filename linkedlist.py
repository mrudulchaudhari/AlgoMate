class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_before(self, target, value):
        if not self.head:
            return False

        if self.head.data == target:
            self.insert_head(value)
            return True

        prev, curr = None, self.head
        while curr and curr.data != target:
            prev, curr = curr, curr.next
        if curr is None:
            return False #Target Not Found

        new_node = Node(value)
        new_node.next = curr
        prev.next = new_node
        return True