# # To evaluate the infix expression using stacks

# class Stack(object):
#     def __init__(self):
#         self.items = []

#     # Method for pushing on to the stack
#     def push(self,item):
#         self.items.append(item)
    
#     #method for popping from the stack
#     def pop(self):
#         return self.items.pop()

#     # method to check if the stack is empty
#     def isEmpty(self):
#         return (self.items == [])

#     def size(self):
#         return len(self.items)
 
# # function to evaluate the expression
# def infixEval(infixExp):
#     operatorStack = Stack()
#     operandStack = Stack()

#     tokenList = infixExp.split()

#     for token in tokenList:
#         if token in "+**/-":
#             operatorStack.push(token)
#         elif token == '(':
#             operatorStack.push(token)
#         elif token == ')':
#             op = operatorStack.pop()
#             operand2 = operandStack.pop()
#             operand1 = operandStack.pop()
#             res = eval(operand1 + op + operand2)
#             operandStack.push(str(res))
#             operatorStack.pop()
#         else:
#             operandStack.push(token)
    
#     while(operandStack.size() != 1):
#         op = operatorStack.pop()
#         operand2 = operandStack.pop()
#         operand1 = operandStack.pop()
#         res = eval(operand1 + op + operand2)
#         operandStack.push(str(res))
    
#     return operandStack.pop()

# # print(infixEval("5 + 4 + ( 3 + 2 ) * 1"))   # output: 14
# # print(infixEval("2 * ( 3 + 5 ) * ( 6 + 4 )"))   # output: 160
# # print(infixEval("( 4 - ( 2 - 4 ) ) * 2"))   # output: 12
# # print(infixEval("10 + 3 * 5 / ( 16 - 4 )")) # output: 11.25
# print(infixEval("( 2 ** 3 ) + ( 9 - 2 )"))