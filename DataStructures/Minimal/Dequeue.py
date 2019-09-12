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

# if __name__ == '__main__':
#     s1 = Dequeue()
#     print(s1.addFront(4))
#     print(s1.addFront(3))
#     print(s1.addRear(2))
#     print(s1.addRear(1))
#     print(s1.items)
#     print(s1.size())
#     print(s1.removeRear())
#     print(s1.removeRear())
#     print(s1.removeFront())
#     print(s1.removeFront())
#     print(s1.isEmpty())