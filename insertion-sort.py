# implementation of insertion_sort algorithm
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        
        while j > 0 and array[j-1] > key:
            array[j] = array[j-1]
            j -= 1

        # place the (key) in its correct position
        array[j] = key

    # return final sorted array
    return array
    

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
