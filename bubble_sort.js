function bubbleSort(array){
    for (let i = 0; i < array.length; i++){
        let hasSwaps = false;
        for (let j = 0; j < (array.length - i) - 1; j++){
            if(array[j] > array[j+1]){
                [array[j], array[j+1]] = [array[j+1], array[j]];
                hasSwaps = true;
            }
        }
        
        // check if no swaps to early exit
        if(!hasSwaps) break;
    }
    
    return array;
}

const arr = [9,53,5,0,2,3,1,4,9];
console.log("sorted: ", bubbleSort(arr));
