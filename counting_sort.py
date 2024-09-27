def counting_sort(arr):
    if not arr:
        return arr
    
    # Step 1: Define min and max values of array
    min_val = min(arr)
    max_val = max(arr)
    
    # Early exit of all elements are equal
    if min_val == max_val:
        return arr
        
    # Step 2: Define the range and create the count array
    range_val = max_val - min_val + 1
    count = [0] * range_val
    
    # Step 3: Fill the count array with the frequency of each element
    for num in arr:
        count[num - min_val] += 1
        
    # Step 4: Modify count array to contain the cumulative sums
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    # Step 5: Create the output array to store the sorted elements
    output = [0] * len(arr)
    
    # Step 6: Place elements in the correct position in the output array
    for num in arr[::-1]: # Note: Reverse in order to maintain stability 
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    # Step 7: Copy the output array elements into the original array
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr
    


arr = [12,3,85,6,89,0,2,1,3,68,74,11]
print("sorted: ", counting_sort(arr))

arr = [6, 56, 1, 32, 0, 9, 2, 23, 0]
print("Sorted array:", counting_sort(arr))
