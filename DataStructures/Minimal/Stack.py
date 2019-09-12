# Implementing a stack 

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# if __name__ == '__main__':
#     s1 = Stack()
#     print(s1.push(1))
#     print(s1.push(2))
#     print(s1.push(3))
#     print(s1.push(4))
#     print(s1.size())
#     print(s1.peek())
#     print(s1.pop())
#     print(s1.pop())
#     print(s1.isEmpty())


    