# Implentation to convert infix expression to postfix expression using a Stack

class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])
    
    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

def infixToPostfix(infix_exp):
    # creating a dictionary for referring the precedence when needed
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    opStack = Stack()
    postfixList = []
    tokenList = infix_exp.split()

    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numerics = '0123456789'
    
    for token in tokenList:
        if token in alphas or token in numerics:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()

            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        
        else:
            while(not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return  " ".join(postfixList)

if __name__ == "__main__":
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("A * B - ( C + D ) + E"))

            

