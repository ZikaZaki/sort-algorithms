function bucketSort(arr, numOfBuckets=10){
  if(arr.length === 0) return arr;
  
  // Step 1: Create buckets based on numOfBuckets argument
  const buckets = Array.from({ length: numOfBuckets }, () => []);

  // Step 2: Define factors used to distribute elements into the buckets
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const range = max - min;

  for
  
  
}
