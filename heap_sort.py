def heapify(array, n, i):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left >= n:
            break

        largest = left

        if right < n and array[right] > array[left]:
            largest = right

        if array[i] >= array[largest]:
            break

        array[i], array[largest] = array[largest], array[i]
        i = largest


def heapsort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

arr = [3,1,4,1,5,9,2,6,5,3,5]    
heapsort(arr)
print("MinHeap after sort: ", arr)   
