# Node is the building block of a linked list, it holds data and a reference to another node like a chain
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Linked List is the class where we define the operations 
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")


L = LinkedList()
L.append(10)
L.append(20)
L.append(30)
L.display()