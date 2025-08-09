def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                print(arr)
        if not swapped:
            print("No swaps made, array is sorted.")
            break
        

def reverseBubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if(arr[j] < arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                print(arr)

        if not swapped:
            print("No swaps made, array is sorted.")
            break

elements = [3, -2, 0, 5, -1, 0, 4]

print(elements)
print("Bubble Sort")
bubbleSort(elements)
print("\n")
print(elements)
print("Reverse Bubble Sort")
reverseBubbleSort(elements)