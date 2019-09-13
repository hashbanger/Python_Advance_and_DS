# Sum of digits using recursion

def sumOfDigits(num):

    if num < 10:
        return num

    else:
        return (num % 10) + sumOfDigits(num // 10)

if __name__ == "__main__":
    num = int(input('Enter the number'))
    print(sumOfDigits(num))