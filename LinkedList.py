# Create a single node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Create a linked list class - a collection of nodes
class LinkedList:
    def __init__(self):
        self.head = None


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

    def update(self, current_value, new_value):
        # Create a new node for the new value
        new_node = Node(new_value)

        # Get the current linked list
        current_node = self.head

        # loop through linked list
        while (current_node):
            # if value to update is later in the linked list
            if (current_node.next):
                if current_node.next.data == current_value:
                    # Assign remaining linked list to new_node.nedt
                    new_node.next = current_node.next.next
                    # Assign current_node's next to the new node
                    # This will look like beginning --> new node --> remaining list
                    current_node.next = new_node

                    # Work through rest of list
                    current_node = current_node.next

            # If value is current (first) node, replace and assign new node
            if current_node.data == current_value:
                # assign remaining linked list to new_node
                new_node.next = current_node.next
                # make the new node the current node and heasd of the linked list
                current_node = new_node
                self.head = current_node

            else:
                # loop through rest of linked list
                current_node = current_node.next

    def delete(self, value_to_delete):
        current_node = self.head
        while(current_node):
            if current_node.next:
                if current_node.next.data == value_to_delete:
                    current_node.next = current_node.next.next
            if current_node.data == value_to_delete:
                self.head = current_node.next

            current_node = current_node.next



    def printlinkedlist(self):
        # print current node
        # iterate through linked list to print each data element
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next
