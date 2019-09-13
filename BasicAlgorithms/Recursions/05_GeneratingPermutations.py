# implementing a recurvsive function to generate
# all combinations of a string

def permute(inp_string):

    out = []

    if len(inp_string) == 1:
        out = [inp_string]

    else:

        for i, letter in enumerate(inp_string):

            for perm in permute(inp_string[:i] + inp_string[i+1:]):

                out += [letter+perm]

    return out

# main

if __name__ == "__main__":
    inp_string = input("Enter the string\n")
    print(permute(inp_string))