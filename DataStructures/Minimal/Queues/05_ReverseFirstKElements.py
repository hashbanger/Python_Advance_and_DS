# Implement a function to reverse the first k elements of a queue.

# Queue implementation
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

    def display(self):
        return self.items[::-1]

# Stack Implementation
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

def reverseFirstK(que, k):
    stk = Stack()
    for _ in range(0, k):
        stk.push(que.dequeue())
    while not stk.isEmpty():
        que.enqueue(stk.pop())
    for _ in range(0, que.size()-k):
        que.enqueue(que.dequeue())
    
# main
if __name__ == "__main__":
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)
    que.enqueue(6)
    que.enqueue(7)
    que.enqueue(8)
    reverseFirstK(que, 3)
    print(que.display())
