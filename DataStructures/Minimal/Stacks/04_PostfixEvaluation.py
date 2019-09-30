# To evaluate the postfix expression using stacks

class Stack(object):
    def __init__(self):
        self.items = []

    # Method for pushing on to the stack
    def push(self,item):
        self.items.append(item)
    
    #method for popping from the stack
    def pop(self):
        return self.items.pop()

    # method to check if the stack is empty
    def isEmpty(self):
        return (self.items == [])

# function to evaluate the expression
def postfixEval(postfixExp):
    operandStack = Stack()
    tokenList = postfixExp.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(token)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = eval(operand1 + token + operand2)
            operandStack.push(str(result))

    return operandStack.pop()

print(postfixEval("1 2 3 * + 5 -"))