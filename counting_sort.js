function countingSort(arr){
    if (arr.length == 0) return arr;
    
    const min = Math.min(...arr);
    const max = Math.max(...arr);
    
    if (min === max) return arr;
    
    const range = max - min + 1;
    const count = Array.from({ length: range }, () => 0);
    
    arr.forEach(element => count[element - min] += 1);
    
    // Calculate the cumulative sums for count arrays
    for(let i = 1; i < count.length; i++){
        count[i] += count[i-1];
    }
    
    const output = Array.from({ length: arr.length }, () => 0);
    
    arr.reverse().forEach(element => {
        output[count[element - min] - 1] = element;
        count[element - min] -= 1;
    });
    
    for(let i = 0; i < arr.length; i++){
        arr[i] = output[i];
    }
    
    return arr;
    
}

const arr = [6, 56, 1, 32, 0, 9, 2, 23, 0];
console.log("sorted:", countingSort(arr));
