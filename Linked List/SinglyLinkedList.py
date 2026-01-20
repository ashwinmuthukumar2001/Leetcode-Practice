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

    #insert node at beginning
    def insertAtBegining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insert node at specific position(0 index based)
    def insertAtIndex(self,data,index):
        new_node = Node(data)
        if index == 0:
            self.insertAtBegining(data)
            return
        
        current = self.head
        for i in range(index-1):
            if current:
                current = current.next
            else:
                print('index exceeds length of the list')
                return

        new_node.next = current.next
        current.next = new_node
        
        
 

L = LinkedList()
L.append(10)
L.append(20)
L.append(30)
L.insertAtBegining(5)
L.insertAtIndex(15,2)
L.insertAtIndex(40,5)

L.insertAtIndex(100,10)

L.display()