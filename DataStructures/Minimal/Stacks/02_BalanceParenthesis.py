# Program to check balanced parenthesis using stack

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

# Logic function

def checkParenthesis(full_string):
    matches = set([ ('[', ']') , ('{', '}'), ('(', ')') ])
    openings = set(['[', '{', '('])
    stack = Stack()

    for i in full_string:
        if i in openings:
            stack.push(i)

        else:

            if stack.size() == 0:
                return False

            last_open  = stack.pop()

            if (last_open, i) not in matches:
                return False
    return stack.size() == 0
        
# main

if __name__ == "__main__":
    full_string = input('Enter the string\n')
    result = checkParenthesis(full_string)
    print(result)
