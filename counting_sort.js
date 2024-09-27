function countingSort(arr){
    if (arr.length == 0) return arr;

    // Step 1: Define min and max values of arr
    const min = Math.min(...arr);
    const max = Math.max(...arr);

    // Early exit if all elements are equal
    if (min === max) return arr;

    // Step 2: Create count array with the size of calculated range + 1
    const range = max - min + 1;
    const count = Array.from({ length: range }, () => 0);

    // Step 3: Calculate the frequency count of each element in original arr
    arr.forEach(element => count[element - min] += 1);
    
    // Step 4: Calculate the cumulative sums for count array
    for(let i = 1; i < count.length; i++){
        count[i] += count[i-1];
    }

    // Step 5: Create the output array with size equal to original array
    const output = Array.from({ length: arr.length }, () => 0);
    // Step 6: Populate the output array with the sorted elements. Note: loop through array in reverse to ensure stability.
    arr.reverse().forEach(element => {
        output[count[element - min] - 1] = element;
        count[element - min] -= 1;
    });

    // Step 7: Copy output to original array
    for(let i = 0; i < arr.length; i++){
        arr[i] = output[i];
    }
    
    return arr;
    
}

const arr = [6, 56, 1, 32, 0, 9, 2, 23, 0];
console.log("sorted:", countingSort(arr));
