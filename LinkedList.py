# Create a single node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Create a linked list class - a collection of nodes
class LinkedList:
    def __init__(self):
        self.head = None

