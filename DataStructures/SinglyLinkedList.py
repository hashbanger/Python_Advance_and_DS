#Creating a class Node

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def listLength(self):
        current = self.head
        length = 0
        while current:
            length = length + 1
            current = current.next
        return length 

    def insertAtBeginning(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            pastHead = self.head
            self.head = newNode
            newNode.next = pastHead
            
    def insertAtEnd(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current:
                previous = current
                current = current.next

            previous.next = newNode

    def insertAt(self, newNode, position):
        if self.listLength() < position:
            print("Position not found")
            return
        else:
            if self.head is None:
                self.head = newNode
            else:
                if position == 1:
                    self.insertAtBeginning(newNode)
                else:
                    current = self.head
                    for _ in range(position-2):
                        current = current.next
                    newNode.next = current.next
                    current.next = newNode

    def printList(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            print('----Current List---\n')
            current = self.head
            while current:
                print(current.data)
                current = current.next
#Creating the list

firstNode = Node('Batman')
linkedlist = LinkedList()
linkedlist.insertAtEnd(firstNode)
secondNode = Node('Superman')
linkedlist.insertAtEnd(secondNode)
thirdNode = Node('WonderWoman')
linkedlist.insertAtBeginning(thirdNode)
fourthNode = Node('Aquaman')
linkedlist.insertAt(fourthNode, 3)
linkedlist.printList()
print("\nLength of list: "+str(linkedlist.listLength())+'\n')