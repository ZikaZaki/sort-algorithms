function mergeSort(arr) {
    
    if (arr.length > 1){
        const midIndex = Math.floor(arr.length / 2);
        const leftArr = arr.slice(0, midIndex);
        const rightArr = arr.slice(midIndex, arr.length);
        
        // left side
        mergeSort(leftArr);
        // right side
        mergeSort(rightArr);
        
        let k = i = j = 0;
        
        while(i < leftArr.length && j < rightArr.length){
            if (leftArr[i] < rightArr[j]){
                arr[k] = leftArr[i];
                i++;
            }else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }
        
        while(i < leftArr.length){
            arr[k] = leftArr[i];
            i++;
            k++;
        }
        
        while(j < rightArr.length) {
            arr[k] = rightArr[j];
            j++;
            k++;
        }
    }
    
    return arr;
}

function merge(arr, temp, left, mid, right) {
    let i = left;     // Starting index of left subarray
    let j = mid + 1;  // Starting index of right subarray
    let k = left;     // Starting index to be sorted in temp array

    // Merge the two subarrays into temp
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k] = arr[i];
            i++;
        } else {
            temp[k] = arr[j];
            j++;
        }
        k++;
    }

    // Copy remaining elements of the left subarray, if any
    while (i <= mid) {
        temp[k] = arr[i];
        i++;
        k++;
    }

    // Copy remaining elements of the right subarray, if any
    while (j <= right) {
        temp[k] = arr[j];
        j++;
        k++;
    }

    // Copy sorted subarray back into the original array
    for (i = left; i <= right; i++) {
        arr[i] = temp[i];
    }
}

function mergeSortIterative(arr) {
    let n = arr.length;
    let temp = new Array(n);  // Temporary array for merging

    // size is the size of subarrays to be merged (1, 2, 4, 8, ...)
    for (let size = 1; size < n; size *= 2) {
        // left is the starting point of the subarrays to be merged
        for (let left = 0; left < n - size; left += 2 * size) {
            let mid = left + size - 1;
            let right = Math.min(left + 2 * size - 1, n - 1);
            merge(arr, temp, left, mid, right);
        }
    }

    return arr;
}

const arr = [53,9,5,9,2,3,1,4,0];
console.log("sorted: ", mergeSort(arr));
