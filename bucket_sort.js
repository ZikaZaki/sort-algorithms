function bucketSort(arr, numOfBuckets=10){
  if(arr.length === 0) return arr;
  
  // Step 1: Create buckets based on numOfBuckets argument
  const buckets = Array.from({ length: numOfBuckets }, () => []);
  
  // Step 2: Define factors used to distribute elements into the buckets
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const range = max - min;

  // Avoid division by zero if all elements are equal
  if(range === 0) return arr;
  
  // Step 3: Calculate the bucket index for each element and insert element in its calculated bucket  
  arr.forEach(element => {
    let index = Math.floor((element - min) / range * (numOfBuckets -1));
    index = Math.min(index, numOfBuckets - 1) // Prevents index out of range
    buckets[index].push(element);
  });
  
  // Step 4: Sort each bucket and concatenate the results. 
  arr = buckets.flatMap(bucket => bucket.sort((a, b) => a - b));

  return arr;
}

const arr = [6, 56, 1, 32, 0, 9, 2, 23, 0]

console.log("sorted:", bucketSort(arr));
