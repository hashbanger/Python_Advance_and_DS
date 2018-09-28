#Bubble Sort
def selectionSort(arr, n):
    for i in range(0, n):
        for j in range(i+1, n-1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr    

if __name__ == '__main__':
    n = int(input("Enter number of elements  "))
    arr = [x for x in map(int, input().split(" "))]
    arr = selectionSort(arr, n)
    print("Sorted array ",arr)