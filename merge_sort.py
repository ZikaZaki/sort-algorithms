# merge-sort iteratively
# =================================================================================

# merge-sort recursively
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


        # handle remainings in the left_half
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        # handle remainings in the right_half
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

arr = [0, 5, 7, 6, 8, 3, 2, 1]
merge_sort(arr)
print("Sorted Array: ", arr)
        
