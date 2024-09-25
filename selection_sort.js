function selectionSort(array){
    for (let i = 0; i < array.length; i++){
        min = i;
        for (let j = i+1; j < array.length; j++){
            if (array[j] < array[min]){
                min = j
            }
        }
        
        // swap the first unsorted element with the minimum element
        [array[i], array[min]] = [array[min], array[i]];
    }
    
    return array;
}

let arr = [56,23,6,2,0,9,1,0,32];
console.log("Sorted: ", selectionSort(arr));
