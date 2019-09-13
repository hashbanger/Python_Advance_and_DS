# A recursive function to find the sum of all numbers upto provided number

def cumSum(num):

    if num == 0:
        return 0

    else:
        return num + cumSum(num-1)

if __name__ == "__main__":
    num = int(input("Enter the number\t"))
    print(cumSum(num))
        