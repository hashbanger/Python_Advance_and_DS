#Implementing Stack using the limited size
#By Prashant Brahmbhatt (linkedin.com/in/prashantbrahmbhatt)

class Stack:
    #Initailizing array of size 10
    def __init__(self):
        self.stack = list()
        self.maxSize = 10
        self.top = 0

    #Adding elements to the Stack
    def push(self, data):
        if self.top < self.maxSize:
            if data not in self.stack:
                self.stack.append(data)
                self.top = self.top + 1
                return True
        else:
            print("Stack Overflow")
            return None

    #Removing the element from the Stack
    def pop(self):
        if self.top <= 0:
            print("Stack underflow")
            return None
        item = self.stack.pop()
        self.top = self.top - 1
        print("\n{} popped\n".format(item))
        return None

    def printStack(self):
        for i in range(self.top):
            print("{}".format(self.stack[i]))
        return None

stack = Stack()
stack.push(4)
stack.push(7)
stack.push(8)
stack.push(9) 
stack.push(10)
stack.push(10)
stack.pop()
stack.printStack()
    
        
        
        
