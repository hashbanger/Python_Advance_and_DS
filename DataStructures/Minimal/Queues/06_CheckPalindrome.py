# Implementing a function to check if a string is palindrome or not using Queues

# Implementing a Dequeue (Double Ended)

class Dequeue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def addFront(self, item):
        self.items.append(item) # considering front to the right of the list
        
    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def checkPalindrome(inpStr):
    charQue = Dequeue()
    for ch in inpStr:
        charQue.addRear(ch)
    isPal = True

    while charQue.size() > 1 and isPal:
        first = charQue.removeFront()
        last = charQue.removeRear()
        if first != last:
            isPal = False
    
    return isPal

# main
if __name__ == "__main__":
    inpStr = input()
    print(checkPalindrome(inpStr))