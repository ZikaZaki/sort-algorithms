def selection_sort(array):
  for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
      if array[j] < array[min_index]:
        min_index = j

    array[i], array[min_index] = array[min_index], array[i]


arr = [5,4,7,2,15,16,11,1]
selection_sort(arr)
print("Sorted Array: ", arr)

