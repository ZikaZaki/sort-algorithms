def counting_sort(arr, exp):
    if not arr:
        return arr
        
    n = len(arr)
    output = [0] * n # Output array which is equal to the size of original array
    count = [0] * 10 # Count array with size of 10 as we're using 10 base numbering

    # Populate the count array with the number of occurances of each number in arr
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Calculate the cumulative sums for count array
    for i in range(1, 10):
        count[i] += count[i-1]

    # Populate the output array with sorted elements. Note: backward traversing is to ensure stability.
    for num in arr[::-1]:
        index = (num // exp) % 10
        count[index] -= 1
        output[count[index]] = num

    # Copy output array to original array
    for i in range(n):
        arr[i] = output[i]
    

def radix_sort(arr):
    if not arr:
        return arr
      
    # Find max element in arr
    max_val = max(arr)
    exp = 1 # Initialize the exponent (1, 10, 100, ...)
    
    while max_val // exp > 0:
        counting_sort(arr, exp) # Sort the elements based on the exponent using count-sort
        exp *= 10 # Move to the next exponent
    
    return arr


    
arr = [12,3,85,6,89,0,2,1,3,68,74,11]
print("sorted: ", radix_sort(arr))

arr = [6, 56, 1, 32, 0, 9, 2, 23, 0]
print("Sorted array:", radix_sort(arr))
