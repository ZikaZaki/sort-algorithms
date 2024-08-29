def merge_sort(array, low=None, high=None):
    if low is None or high is None:
        low, high = 0, len(array) - 1

    if (low < high):
        mid = (low + high) // 2
        if (high - low) == 1:
            if array[low] > array[high]:
                array[low], array[high] = array[high], array[low]

        
        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, high)
        
        for i in range(low, mid+1):
            if (array[i] > array[mid+1]):
                array[i], array[mid+1] = array[mid+1], array[i]
    
    return array
        
    
        
arr = [2,1,0,5,7,6,8,3]
print(merge_sort(arr))
