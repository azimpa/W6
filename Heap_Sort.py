def heapify(arr, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < N and arr[largest] < arr[left]:
        largest = left

    if right < N and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, N, largest)

def heapSort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    heapSort(arr)
    N = len(arr)

    print("Sorted array is")
    for i in range(N):
        print(arr[i], end=" ")