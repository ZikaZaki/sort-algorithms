def bubble_sort(array):
  for i in range(len(array)):
    has_swaps = False
    for j in range(0, len(array)-i-1):
      if(array[j] > array[j+1]):
        array[j], array[j+1] = array[j+1], array[j]
        has_swaps = True

    # check if there's no swap to early exit
    if(not has_swaps):
      break

arr = [9,53,5,0,2,3,1,4,9]
bubble_sort(arr)
print(arr)
