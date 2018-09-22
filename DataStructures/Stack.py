#Implementing a stack

class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        #Checking if entry exists
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            print("Duplicate Entry")
            return None

    #Removing the Top element of the Stack
    def pop(self):
        if len(self.stack) <= 0:
            print("Stack is Empty")
            return None
        return self.stack.pop()

    def printStack(self):
        if len(self.stack) <= 0:
            print("Stack Empty")
            return None
        print("\nElements of the Stack are\n")
        for i in self.stack:
            print("{} ".format(i))
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
