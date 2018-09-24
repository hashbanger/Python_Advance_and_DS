#Implementing a doubly linked list
class Node:
    #Initializing the Node
    def __init__(self, data= None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:

    #Initializing the head
    def __init__(self):
        self.head = None
    #Finding the length
    def listLength(self):
        current = self.head
        length = 0
        while current:
            length = length + 1
            current = current.next
        return length 
    
    #Inserting at beginning
    def insertAtBeginning(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
    #Inserting at the end
    def insertAtEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next!= None:
                current = current.next

            current.next = newNode
            newNode.prev = current
    #Inserting at the desired position
    def insertAt(self, newNode, position):
        if self.listLength() < position:
            print("Position invalid")
            return None
        else:
            if self.head is None:
                self.head = newNode
            else:
                current = self.head
                for _ in range(1, position-1):
                    current = current.next

                current.next.prev = newNode
                newNode.next = current.next
                newNode.prev = current
                current.next = newNode
                 

    
    #Deleting from the beginning
    def deleteFromFront(self):
        if self.head is None:
            print("List is empty")
            return None
        else:
            deleteNode = self.head
            self.head = self.head.next
            self.head.prev = None
            del deleteNode

    #Delete from the end
    def deleteFromEnd(self):
        if self.head is None:
            print("List is Empty")
            return None
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            
            deleteNode = current.next
            current.next = None
            del deleteNode

    def deleteFrom(self, position):
        if self.listLength() < position:
            print("Position Invalid")
            return None
        else:
            if position is 1:
                self.deleteFromFront()
            else:
                current = self.head
                for _ in range(1, position -1 ):
                    current = current.next

                deleteNode = current.next
                current.next = current.next.next
                current.next.prev = current
                del deleteNode
            
    #Displaying the list
    def printList(self):
        if self.head is None:
            print("List is empty")
            return None
        else:
            current = self.head
            print("----Current List----")
            while current:
                print(current.data)
                current = current.next

if __name__ == '__main__':
    linkedlist = LinkedList()
    firstNode = Node('Batman')
    linkedlist.insertAtBeginning(firstNode)
    secondNode = Node('Superman')
    linkedlist.insertAtEnd(secondNode)
    thirdNode = Node('WonderWoman')
    linkedlist.insertAtBeginning(thirdNode)
    fourthNode = Node('Aquaman')
    linkedlist.insertAtBeginning(fourthNode)
    fifthNode = Node ('Cyborg')
    linkedlist.insertAt(fifthNode ,3)
    linkedlist.printList()
    print()
    linkedlist.deleteFromEnd()
    linkedlist.printList()
    print()
    linkedlist.deleteFrom(2)
    linkedlist.printList()

        
            
            
        
