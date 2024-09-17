# Iterative implementation of the merge-sort algorithm
def merge(left, right):
    result = []
    i = j = 0

    # Merge the two lists together
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    
    # Iterate through the list, doubling the width of subarrays to merge each time
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        
        # Double the subarray width
        width *= 2

    return arr

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort_iterative(arr)
print("Sorted array:", sorted_arr)

# =================================================================================

# Recursive implementation of the merge-sort algorithm
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        merge_sort(left_half) # recursive call with the left side
        merge_sort(right_half) # recursive call with the right side

        # k: point to original (array), i: to (left_half), j: to (right_half)
        k = i = j = 0

        # compare sorted left and right and then insert/replace into original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            # increment (k) pointer after every insert/replace from (left or right)
            k += 1


        # handle remaining elements in the left_half
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        # handle remaining elements in the right_half
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

arr = [0, 5, 7, 6, 8, 3, 2, 1]
merge_sort(arr)
print("Sorted Array: ", arr)
        
