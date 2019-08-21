#Implementing a Circular Linked list

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    #initializing the head
    def __init__(self):
        self.head = None        

    #Finding the length of the list
    def listLength(self):
        current = self.head
        length = 0
        while current.next!= self.head:
            length = length + 1
            current = current.next
        return length 

    #inserting at the beginning 
    def insertAtBeginning(self, newNode):
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            newNode.next = self.head
            self.head = newNode
            #Now traversing to last node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode

    #Inserting at the end of the list
    def insertAtEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head  

#Inserting at desired positon
    def insertAt(self,newNode, position):
        if self.listLength < position:
            print("Invalid Position")
            return None
        else:
            if self.head is None:
                self.head = newNode
            else:
                if position == 1:
                    self.insertAtBeginning(newNode)
                else:
                    current = self.head
                    for _ in range(1,position-1):
                        current = current.next

                    newNode.next = current.next
                    current.next = newNode

#Deleting the node from the beginning
    def deleteFromBeginning(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            self.head = self.head.next
            del current

#Deleting from the end
    def deleteFromEnd(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        else:
            current = self.head
            while current.next.next :
                current = current.next
            deleteNode = current.next
            current.next = self.head
            del deleteNode
            
#Deleting from desired place
    def deleteFrom(self, position):
        if self.listLength() < position:
            print("Position not found")
            return None
        else:
            if position == 1:
                self.deleteFromBeginning()
            else:
                current = self.head
                for _ in range(1,position-1):
                    current = current.next
                deleteNode = current.next
                current.next = deleteNode.next

#Displaying the list   

    def printList(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            print('----Current List---\n')
            current = self.head
            while current.next != self.head:
                print(current.data)
                current = current.next
#Creating the list
if __name__ == '__main__':
    firstNode = Node('Batman')
    linkedlist = LinkedList()
    linkedlist.insertAtEnd(firstNode)
    linkedlist.printList()
    secondNode = Node('Superman')
    linkedlist.insertAtEnd(secondNode)
    thirdNode = Node('WonderWoman')
    linkedlist.insertAtBeginning(thirdNode)
    fourthNode = Node('Aquaman')
    linkedlist.insertAt(fourthNode, 3)
    fourthNode = Node('Cyborg')
    linkedlist.insertAt(fourthNode, 2)
    linkedlist.printList()
    linkedlist.deleteFromEnd()
    linkedlist.printList()
    linkedlist.deleteFromBeginning()
    linkedlist.printList()
    linkedlist.deleteFrom(2)
    linkedlist.printList()
    print("\nLength of list: "+str(linkedlist.listLength())+'\n')

