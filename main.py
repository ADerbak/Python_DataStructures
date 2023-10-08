from LinkedList import LinkedList, Node

# ll = LinkedList()
# ll.head = Node(3)
# print(ll.head.data)


ll = LinkedList()
ll.insert('a')
ll.insert('b')
ll.insert('c')
ll.insert('d')
ll.update('d','e')
ll.update('c','g')
ll.delete('a')
ll.delete('b')
ll.printlinkedlist()
