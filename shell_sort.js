function shellSort(arr){
    if(arr.length === 0) return arr;
    
    const n = arr.length;
    let gap = Math.floor(n / 2);
    
    while (gap > 0){
        for (let i = gap; i < n; i++){
            let temp = arr[i];
            let j = i;
            
            while (j >= gap && arr[j-gap] > temp){
                arr[j] = arr[j-gap];
                j -= gap;
            }
            // replace j with temp
            arr[j] = temp;
        }
        
        gap = Math.floor(gap / 2);
    }
    
    return arr;
}

let arr = [56,23,6,2,0,9,1,0,32];
console.log("Sorted: ", shellSort(arr));
