# Implementing a function for fibonacci sequence using recursion

def fibonacci(n):
    
    if n ==1 or n ==0:
        return n

    else:
        return fibonacci(n-1) + fibonacci(n-2)

# main

if __name__ == "__main__":
    n = int(input("Enter the term you want.\t"))
    print(fibonacci(n))