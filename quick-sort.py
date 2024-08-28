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
  high = high or (len(array) - 1)
  
  if (low < high):
    pivot_index = partition(array, low, high)

    print("Array: ", array)
    quick_sort(array, low, pivot_index - 1)
    quick_sort(array, pivot_index + 1, high)
