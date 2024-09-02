# Quick Sort Iteratively
# Pivot from end
def partition(arr, start, end):
    pivot = arr[end]
    i = end
    
    for j in range(end-1, start-1, -1):
        if arr[j] >= pivot:
            i -= 1
            arr[i], arr[j] = arr[j], arr[i]
            
    
    arr[i], arr[end] = arr[end], arr[i]
    
    return i

# Pivot from start
def partition(arr, start, end):
    pivot = arr[start]
    i = start
    
    for j in range(start+1, end+1):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[start], arr[i] = arr[i], arr[start]
    
    return i
    

def quick_sort(arr):
    stack = [(0, len(arr)-1)]
    
    while stack:
        start, end = stack.pop()
        
        if start < end:
            pivot_index = partition(arr, start, end)
            
            stack.append((start, pivot_index - 1))
            stack.append((pivot_index + 1, end))
            
    return arr
    
print(quick_sort([4,23,6,2,5,9,7,0,1]))
print(quick_sort([4,2,5,6,0,1]))

# ===============================================================================

# Quick Sort recursively==============================
def partition(arr, low, high):
  pivot = arr[high]
  i = low
  
  for j in range(low, high):
    if (arr[j] <= pivot):
      arr[i], arr[j] = arr[j], arr[i]
      i += 1

  arr[i], arr[high] = arr[high], arr[i]
  return i


def quick_sort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1
  
  if (low < high):
    pivot_index = partition(array, low, high)

    print("Array: ", array)
    quick_sort(array, low, pivot_index - 1)
    quick_sort(array, pivot_index + 1, high)
