#Bubble Sort
def bubbleSort(arr, n):
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr    

if __name__ == '__main__':
    n = int(input("Enter number of elements  "))
    arr = [x for x in map(int, input().split(" "))]
    arr = bubbleSort(arr, n)
    print("Sorted array ",arr)