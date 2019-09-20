# Implementing a Dynamic Stack
# # We will double the size of the stack when the stack overflows 

class Stack(object):

    def __init__(self, limit = 10, top = -1): # setting the default limit to 10
        self.stk = [None] * limit
        self.limit = limit
        self.top = top

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        self.top += 1
        self.stk[self.top] = item
        if self.top+1 == self.limit:
            self.resize()

    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")
            return 0
        else:
            return self.stk[-1]

    def resize(self):
        newStk = list(self.stk)+ ([None] * self.limit)
        self.stk = newStk       
        self.limit = 2 * self.limit

    def size(self):
        return len(self.stk)

if __name__ == '__main__':
    s1 = Stack(limit=5)
    s1.push("A")
    s1.push("B")
    s1.push("C")
    s1.push("D")
    print(s1.stk)
    s1.push("E")
    s1.push("F")
    s1.push("A")
    s1.push("B")
    s1.push("C")
    # s1.push("D")
    print(s1.stk)
    print(s1.size())
    print(s1.pop())
    print(s1.pop())
    print(s1.peek())
    print(s1.isEmpty())
    print(s1.stk)