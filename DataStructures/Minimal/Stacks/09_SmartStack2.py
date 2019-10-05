# A smart stack maintains a second stack for the minimum of the stack at each push operation
# In this we will improve space complexity by only pushing if the new minimum or minimum 
# same as current is encountered and popping only when main stack element and 
# min stack element matches
# Example:
# main_stack    min_stack
#   1
#   5               
#   1               
#   4               1
#   6               1
#   2               2

class SmartStack(object):
    def __init__(self):
        self.stack = []
        self.min = []

    def smartPush(self, item):
        self.stack.append(item)
        if not self.min or item <= self.stackMin():
            self.min.append(item)

    def smartPop(self):
        x = self.stack.pop()
        if x == self.stackMin():
            self.min.pop()

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
    ss1.smartPush(1)
    print(ss1.stackMin())
    ss1.smartPop()
    ss1.smartPop()
    print(ss1.stackMin())