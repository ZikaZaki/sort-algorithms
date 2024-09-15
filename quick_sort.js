// Quick Sort iterative implementation
function partition(arr, low, high){
    const pivot = arr[high];
    let i = low - 1;
    
    for(let j = low; j < high; j++){
        if(arr[j] <= pivot){
            i += 1;
            // to skip unnecessary swaps use: if (i === j) continue; 
            [arr[i], arr[j]] = [arr[j], arr[i]]
        }
    }
    
    [arr[i+1], arr[high]] = [arr[high], arr[i+1]];
    return i+1;
}


function quickSort(arr){
    const stack = [[0, arr.length - 1]];
    
    while (stack.length > 0){
        const [low, high] = stack.pop();
        
        if(low < high){
            const pivotIndex = partition(arr, low, high);

            // left side
            stack.push([low, pivotIndex - 1]);
            // right side
            stack.push([pivotIndex + 1, high]);
        }
    }
    
    return arr;
}

const arr = [53,9,5,9,2,3,1,4,0];
console.log("sorted: ", quickSort(arr));
