function insertionSort(arr){
    for (let i = 1; i < arr.length; i++){
        const key = arr[i];
        let j = i;
        
        while(j > 0 && arr[j-1] > key){
            arr[j] = arr[j-1];
            j -= 1;
        }
        
        // place the (key) in its correct position
        arr[j] = key;
    }
    
    return arr;
}

const arr = [53,9,5,0,2,3,1,4,9];
console.log("sorted: ", insertionSort(arr));
