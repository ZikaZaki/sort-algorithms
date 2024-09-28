function countingSort(arr, exp){
    if (!arr.length) return arr;
    
    const n = arr.length;
    const output = Array.from({length: n}, () => 0);
    const count = Array.from({length: 10}, () => 0);
    
    // Calculate the occurances count for each element in arr
    for (const element of arr) {
        const index = Math.floor(element / exp) % 10;
        count[index] += 1;
    };
    
    // Caclulate the cumulative sums for count array
    for(let i = 1; i < 10; i++){
        count[i] += count[i-1];
    }
    
    // Populate the output array with sorted elements. 
    // Note: loop in reverse to maintain stability
    for (const element of arr.reverse()) {
        const index = Math.floor(element / exp) % 10;
        count[index] -= 1; // Decrement count
        output[count[index]] = element;
    };
    
    // Copy sorted output array to original array
    for(let i = 0; i < n; i++){
        arr[i] = output[i];
    }
}

function radixSort(arr){
    if (!arr.length) return arr;
    
    // Get maximum element in arr
    const max = Math.max(...arr);
    let exp = 1; // Initialize exponent (1, 10, 100, 1000, ....)
    
    while(Math.floor(max / exp) > 0){
        countingSort(arr, exp);
        exp *= 10; // Move to next exponent
    }
    
    return arr;
}

const arr = [6, 56, 1, 32, 0, 9, 2, 23, 0];
console.log("sorted:", radixSort(arr));
