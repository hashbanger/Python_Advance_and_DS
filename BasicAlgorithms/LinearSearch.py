def linearSearch(arr,n,key):
    for i in range(n):
        if arr[i] is key:
            return i
    return None

def linearSearch_while(arr, n ,key):
    i = 0
    while i<n:
        if arr[i] is key:
            return i
        else:
            i+=1
    return None

if __name__ == '__main__':
    n = int(input("Enter number of elements"))
    arr = [x for x in map(int, input().split(" "))]
    key = int(input("Enter the element to search"))
    i = linearSearch_while(arr, n, key)
    if i!= None:
        print("Number found at {}".format(i+1))
    else:
        print("Number not found")
