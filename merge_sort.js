// Iterative implementation of the Merge Sort algorithm
function merge(left, right) {
    let result = [];
    let i = 0, j = 0;

    // Merge the two lists together
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            result.push(left[i]);
            i++;
        } else {
            result.push(right[j]);
            j++;
        }
    }

    // Add remaining elements
    result = result.concat(left.slice(i)).concat(right.slice(j));
    
    return result;
}

function mergeSortIterative(arr) {
    let width = 1;
    let n = arr.length;

    // Iterate through the list, doubling the width of subarrays to merge each time
    while (width < n) {
        for (let i = 0; i < n; i += 2 * width) {
            let left = arr.slice(i, i + width);
            let right = arr.slice(i + width, i + 2 * width);
            arr.splice(i, 2 * width, ...merge(left, right));
        }
        // Double the subarray width
        width *= 2;
    }

    return arr;
}

// Example usage
let arr = [38, 27, 43, 3, 9, 82, 10];
let sortedArr = mergeSortIterative(arr);
console.log("Sorted array:", sortedArr);
// ================================================================================================

// Recursive implementation of the Merge Sort algorithm
function mergeSort(arr) {
    if (arr.length > 1){
        const midIndex = Math.floor(arr.length / 2);
        const leftArr = arr.slice(0, midIndex);
        const rightArr = arr.slice(midIndex, arr.length);
        
        // recursive call with left side
        mergeSort(leftArr);
        // recursive call with right side
        mergeSort(rightArr);
        
        let k = 0, i = 0, j = 0;
        
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

const arr = [53,9,5,9,2,3,1,4,0];
console.log("sorted: ", mergeSort(arr));
