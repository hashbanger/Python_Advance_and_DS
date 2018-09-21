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
            
    #Displaying the list
    def printList(self):
        current = self.head
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
    linkedlist.deleteFromEnd()
    linkedlist.printList()

        
            
            
        
