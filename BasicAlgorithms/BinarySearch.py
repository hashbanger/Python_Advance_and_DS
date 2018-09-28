#Binary Search

def binarySearch(arr,n , key):
    begin = 0
    end = n
    while begin <= end:
        mid = (begin + end)//2
        if key is arr[mid]:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            begin = mid + 1
        mid = (begin + end)//2
    if begin > end:
        return None

if __name__ == '__main__':
    n = int(input("Enter number of elements  "))
    arr = [x for x in map(int, input().split(" "))]
    key = int(input("Enter the element to search  "))
    i = binarySearch(arr, n, key)
    if i!= None:
        print("Number found at {}".format(i+1))
    else:
        print("Number not found")

