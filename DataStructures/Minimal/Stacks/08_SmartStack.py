# A smart stack maintains a second stack for the minimum of the stack at each push operation
# Example:
# main_stack    min_stack
#   5               1
#   1               1
#   4               2
#   6               2
#   2               2

class SmartStack(object):
    def __init__(self):
        self.stack = []
        self.min = []

    def smartPush(self, item):
        self.stack.append(item)
        if not self.min or item < self.stackMin():
            self.min.append(item)
        else:
            self.min.append(self.min[-1])

    def smartPop(self):
        x = self.stack.pop()
        self.min.pop()
        return x

    def stackMin(self):
        return self.min[-1]

# main
if __name__ == "__main__":
    ss1 = SmartStack()
    ss1.smartPush(2)
    ss1.smartPush(6)
    ss1.smartPush(4)
    print(ss1.stackMin())
    ss1.smartPush(1)
    print(ss1.stackMin())
    ss1.smartPush(5)
    print(ss1.stackMin())
    ss1.smartPop()
    ss1.smartPop()
    print(ss1.stackMin())



