function bucketSort(arr, numOfBuckets=10){
  if(arr.length === 0) return arr;

  const buckets = Array.from({ length: numOfBuckets }, () => []);

  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const range = max - min;
  
  
}
