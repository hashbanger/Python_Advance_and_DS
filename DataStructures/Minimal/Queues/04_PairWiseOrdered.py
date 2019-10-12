# Given a stack of numbers check if the each successive pair is consecutive or not.
# Example [1, 2, -3, -4, 12, 13] should return True

# Implementing a queue
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

# Implementing a stack
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (len(self.items) == 0)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# the core function
import math

def checkStackPairwise(stk):
    que = Queue()
    pairwiseOrdered = True
    # Reversing the elements
    while not stk.isEmpty():
        que.enqueue(stk.pop())
    while not que.isEmpty():
        stk.push(que.dequeue())
    while not stk.isEmpty():
        n = stk.pop()
        que.enqueue(n)
        if not stk.isEmpty():
            m = stk.pop()
            que.enqueue(m)
            if(abs(n-m)!=1):
                pairwiseOrdered = False
                break
    while not que.isEmpty():
        stk.push(que.dequeue())
    return pairwiseOrdered

if __name__ == '__main__':
    s1 = Stack()
    s1.push(4)
    s1.push(5)
    s1.push(-2)
    s1.push(-1)
    s1.push(11)
    s1.push(10)
    s1.push(5)
    s1.push(6)
    s1.push(8)
    print(checkStackPairwise(s1))

