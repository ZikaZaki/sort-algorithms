# Swap helper method to swap array elements
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

# insertion_sort: from start-to-end of array
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap(arr, j-1, j)
            # decrement j to compare (j-1) with previous values till (0)
            j -= 1

    # print final sorted array
    print(f"Final Sorted: {arr}")
    return arr

# reversed_insertion_sort: from end-to-start of array
def reversed_insertion_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = i
        while j < len(arr) and arr[j-1] > arr[j]:
            print(f"Compared: ({arr[j-1]}, {arr[j]})")
            swap(arr, j-1, j)
            print(f"Swapped: {arr}")
            j += 1

    # Print final sorted array
    print(f"Final Sorted: {arr}")
    return arr

my_list = [3,0,1,8,7,2,5,4,9,6]

insertion_sort(my_list)
reversed_insertion_sort(my_list)
