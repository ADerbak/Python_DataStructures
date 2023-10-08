# Create a single node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Create a linked list class - a collection of nodes
class LinkedList:
    def __init__(self):
        self.head = None

    #TODO define insert, update, delete, and print methods
    def insert(self, data):
        # create a new node
        new_node = Node(data)
        # Check to see if there is a head value
        if(self.head):
            current_node = self.head
            # iterate through LL, once next = None, add new node as current.next to previous node
            while (current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        # if not, make the new node the head.
        else:
            self.head = new_node

    def update(self, data):
        pass

    def delete(self):
        pass

    def printlinkedlist(self):
        # print current node
        # iterate through linked list to print each data element
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next
