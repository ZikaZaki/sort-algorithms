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
    

# reversed_insertion_sort
def reversed_insertion_sort(array):
    for i in range(len(array)-1, -1, -1):
        key = array[i]
        j = i

        while j+1 < len(array) and array[j+1] < key:
            array[j] = array[j+1]
            j += 1

        # place the (key) in its correct position
        array[j] = key

    # return final sorted array
    return array

arr = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]

print(insertion_sort(arr))
print(reversed_insertion_sort(arr))
