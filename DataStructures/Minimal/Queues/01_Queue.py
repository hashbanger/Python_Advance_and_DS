# Implementing a Queue

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# if __name__ == '__main__':
#     s1 = Queue()
#     print(s1.enqueue(1))
#     print(s1.enqueue(2))
#     print(s1.enqueue(3))
#     print(s1.enqueue(4))
#     print(s1.size())
#     print(s1.dequeue())
#     print(s1.dequeue())
#     print(s1.isEmpty())