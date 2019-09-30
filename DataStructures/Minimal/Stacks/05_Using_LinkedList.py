# Implementing a stack using a linked list

# Node of a singly linked list
class Node(object):
    def __init__(self):
        self.data = None
        self.next = None

    # method to set the data field of the node
    def setData(self, data):
        self.data = data

    # method to get the data field
    def getData(self):
        return self.data

    # method to set the next field of the node
    def setNext(self, next):
        self.next = next

    # method to get the next field of the node
    def getNext(self):
        return self.next

    # method to check if next node exists
    def hasNext(self):
        return self.next != None

# Creating the Stack class
class Stack(object):
    def __init__(self, data = None):
        self.head = None
        if data:
            for d in data:
                self.push(d)
    
    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head == None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()

# main 
if __name__ == "__main__":
    myList = [1,2,3,4,5,6]
    myStack = Stack(myList)
    print(myStack.peek())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.peek())
