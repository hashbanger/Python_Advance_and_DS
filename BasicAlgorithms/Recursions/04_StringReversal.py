# Implementing a function to reverse using Recursion

def reverse(inp_string):

    if len(inp_string) == 1:
        return inp_string

    else:
        return reverse(inp_string[1:]) + inp_string[0]

if __name__ == "__main__":
    inp_string = input('Enter the string to reverse\n')
    print(reverse(inp_string))