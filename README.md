# Sorting Algorithms
- [x] Bubble Sort
- [x] Insertion Sort
- [ ] Selection Sort
- [x] Merge Sort
- [ ] Shell Sort
- [ ] Heap Sort
- [ ] Bucket Sort
- [ ] Counting Sort
- [ ] Radix Sort
- [x] Quick Sort

| # |       Name      | Stable | Best | Average | Worst | When to Use |
|---|:---------------:|--------|------|---------|-------|----------|
| 1 | Bubble Sort | Yes | **O(n)** <br> <small>(when the array is already sorted)</small> | **O(n<sup>2</sup>)** | **O(n<sup>2</sup>)** | when to use description |
| 2 | Insertion Sort | Yes | **O(n)** <br> (when the array is already sorted) | **O(n<sup>2</sup>)** | **O(n<sup>2</sup>)** | when to use description |
| 3 | Selection Sort | No | **O(n<sup>2</sup>)** | **O(n<sup>2</sup>)** | **O(n<sup>2</sup>)** | when to use description |
| 4 | Quick Sort | No <br> (can be made stable with modifications) | **O(n log n)** | **O(n log n)** | **O(n<sup>2</sup>)** <br> (when the pivot selection is poor, such as always selecting the smallest or largest element | when to use description |


<table style="width: 100%;">
  <thead>
    <tr>
      <th>#</th>
      <th>Name</th>
      <th>Stable</th>
      <th>Best</th>
      <th>&nbsp; &nbsp; &nbsp;Average &nbsp; &nbsp; &nbsp;</th>
      <th>Worst</th>
      <th>When to Use</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td style="white-space: nowrap; text-align: center;">Bubble Sort</td>
      <td>Yes</td>
      <td><strong>O(n)</strong><br>(when array is sorted)</td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Simple to implement; primarily <br> for educational purposes.</p></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Insertion&nbsp;Sort</td>
      <td>Yes</td>
      <td><strong>O(n)</strong><br>(when array is sorted)</td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Efficient for small datasets <br>and nearly sorted arrays.</p></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Selection&nbsp;Sort</td>
      <td>No</td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Useful when memory is limited;<br>not suitable for large datasets.</p></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Quick Sort</td>
      <td >No <br>(can be stable)</td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong><br>(when pivot selection is poor)</td>
      <td><p>Quick Sort is generally the fastest and most efficient for large datasets when memory usage is a concern, especially with large, unsorted arrays where stability is not a requirement.</p></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Merge Sort</td>
      <td>Yes</td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><p>Stable and efficient for large datasets; ideal for linked lists and external sorting.</p></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Heap Sort</td>
      <td>No</td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><p>Good for memory-constrained environments; not stable but performs well on large datasets.</p></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Counting&nbsp;Sort</td>
      <td>Yes</td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n + k)</strong></td>
      <td><p>Best for sorting integers or objects with small ranges; very efficient for large datasets.</p></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Radix Sort</td>
      <td>Yes</td>
      <td><strong>O(nk)</strong></td>
      <td><strong>O(nk)</strong></td>
      <td><strong>O(nk)</strong></td>
      <td><p>Best for sorting large sets of integers; works well when the range of input values is known.</p></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Shell Sort</td>
      <td>No</td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n<sup>3/2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Good for medium-sized arrays; improves on Insertion Sort by comparing elements far apart.</p></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Bucket Sort</td>
      <td>Yes</td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Best for uniformly distributed data; suitable for floating-point numbers.</p></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Tim Sort</td>
      <td>Yes</td>
      <td><strong>O(n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><p>Used in Python's sorted() and Java's Arrays.sort(); efficient for real-world data.</p></td>
    </tr>
  </tbody>
</table>
