def shell_sort(arr):
  if not arr:
    return arr
    
  n = len(arr)
  gap = n // 2
  
  while gap > 0:
    for i in range(gap, n):
      temp = arr[i]
      j = i

      while j >= gap and arr[j-gap] > temp:
        arr[j] = arr[j-gap]
        j -= gap

      arr[j] = temp

    gap //= 2

  return arr


  # Example usage
arr = [0, 0, 1, 2, 6, 9, 32, 23, 56]
print("Sorted array:", shell_sort(arr))
    
