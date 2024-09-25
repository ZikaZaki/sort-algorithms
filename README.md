# Sorting Algorithms
- [x] Selection Sort
- [x] Bubble Sort
- [x] Insertion Sort
- [x] Shell Sort
- [x] Merge Sort
- [x] Quick Sort
- [x] Heap Sort
- [ ] Bucket Sort
- [ ] Counting Sort
- [ ] Radix Sort

<table style="width: 100%;">
  <thead>
    <tr>
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
      <td style="white-space: nowrap; text-align: center;">Bubble Sort</td>
      <td>Yes</td>
      <td><strong>O(n)</strong><br>(when&nbsp;array is&nbsp;sorted)</td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Simple to implement; primarily <br> for educational purposes.</p></td>
    </tr>
    <tr>
      <td>Insertion&nbsp;Sort</td>
      <td>Yes</td>
      <td><strong>O(n)</strong><br>(when array is sorted)</td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Efficient for small datasets <br>and nearly sorted arrays.</p></td>
    </tr>
    <tr>
      <td>Selection&nbsp;Sort</td>
      <td>No</td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Useful when memory is limited;<br>not suitable for large datasets.</p></td>
    </tr>
    <tr>
      <td>Quick Sort</td>
      <td >No <br>(can be stable)</td>
      <td><strong>O(n&nbsp;log&nbsp;n)</strong></td>
      <td><strong>O(n&nbsp;log&nbsp;n)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong><br>(when pivot selection is poor)</td>
      <td><p>Quick Sort is generally the fastest and most efficient for large datasets when memory usage is a concern, especially with large, unsorted arrays where stability is not a requirement.</p></td>
    </tr>
    <tr>
      <td>Merge Sort</td>
      <td>Yes</td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><p>Stable and efficient for large datasets; ideal for linked lists and external sorting.</p></td>
    </tr>
    <tr>
      <td>Heap Sort</td>
      <td>No</td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><p>Good for memory-constrained environments; not stable but performs well on large datasets.</p></td>
    </tr>
    <tr>
      <td>Shell Sort</td>
      <td>No</td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n<sup>3/2</sup>)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Good for medium-sized arrays; improves on Insertion Sort by comparing elements far apart.</p></td>
    </tr>
    <tr>
      <td>Counting&nbsp;Sort</td>
      <td>Yes</td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n + k)</strong></td>
      <td><p>Best for sorting integers or objects with small ranges; very efficient for large datasets.</p></td>
    </tr>
    <tr>
      <td>Radix Sort</td>
      <td>Yes</td>
      <td><strong>O(nk)</strong></td>
      <td><strong>O(nk)</strong></td>
      <td><strong>O(nk)</strong></td>
      <td><p>Best for sorting large sets of integers; works well when the range of input values is known.</p></td>
    </tr>
    <tr>
      <td>Bucket Sort</td>
      <td>Yes</td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n + k)</strong></td>
      <td><strong>O(n<sup>2</sup>)</strong></td>
      <td><p>Best for uniformly distributed data; suitable for floating-point numbers.</p></td>
    </tr>
    <tr>
      <td>Tim Sort</td>
      <td>Yes</td>
      <td><strong>O(n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><strong>O(n log n)</strong></td>
      <td><p>Used in Python's sorted() and Java's Arrays.sort(); efficient for real-world data.</p></td>
    </tr>
  </tbody>
</table>


The time complexity of heap operations depends on the type of heap (e.g., binary heap, Fibonacci heap) and the specific operation. Here, we'll focus primarily on **binary heaps**, which are commonly used in implementations of priority queues.

### Binary Heap Operations Time Complexity

1. **Insertion (`insert`)**:
   - **Average and Worst-Case**: **O(log n)**
   - Insertion involves adding the element at the end of the heap (last position), and then performing an **up-heap** or **bubble-up** operation to maintain the heap property. This takes logarithmic time since, in a binary heap, the height of the tree is proportional to **log n**.

2. **Deletion of the Minimum/Maximum (`deleteMin` or `deleteMax`)**:
   - **Average and Worst-Case**: **O(log n)**
   - Deleting the root element (the minimum in a min-heap, or the maximum in a max-heap) involves replacing the root with the last element and performing a **down-heap** or **heapify-down** operation to restore the heap property. This also takes **O(log n)** time.

3. **Extract Min/Max (`extractMin` or `extractMax`)**:
   - **Average and Worst-Case**: **O(log n)**
   - This operation is essentially the same as deletion: it removes the root (min or max) and re-heapifies the tree.

4. **Peek (Get Min/Max)**:
   - **Average and Worst-Case**: **O(1)**
   - The minimum (or maximum) element is always at the root of the heap, so accessing it is a constant time operation.

5. **Heapify** (Building a heap from an arbitrary array):
   - **Average and Worst-Case**: **O(n)**
   - This operation involves turning an unsorted array into a valid heap. Using the **bottom-up heap construction** algorithm, this operation can be performed in linear time, despite the intuition that heapifying each element would take **O(log n)** per element. The efficiency comes from the fact that more work is done near the bottom of the heap, where there are more nodes with smaller heights.

6. **Decrease Key (or Increase Key)**:
   - **Average and Worst-Case**: **O(log n)**
   - This operation involves modifying the value of a node and then restoring the heap property by either performing an up-heap (if the key was decreased) or a down-heap (if the key was increased).

7. **Merge (Merging two heaps)**:
   - **Average and Worst-Case**: **O(n)**
   - Merging two binary heaps typically involves inserting all the elements from one heap into another, leading to an **O(n log n)** complexity. However, in certain heap types like **Fibonacci heaps**, the merge operation can be more efficient.

### Fibonacci Heap Operations Time Complexity

For comparison, here's a quick look at **Fibonacci heap** operation complexities, which are more efficient for certain operations:

| Operation        | Time Complexity |
|------------------|-----------------|
| **Insert**       | O(1)            |
| **Extract Min**  | O(log n)        |
| **Peek (Min)**   | O(1)            |
| **Decrease Key** | O(1)            |
| **Merge**        | O(1)            |
| **Delete**       | O(log n)        |
| **Heapify**      | O(n)            |

In **Fibonacci heaps**, the key operations like insert, decrease key, and merge are more efficient (constant time), while extracting the minimum and deletion are logarithmic in the number of nodes.

### Summary of Binary Heap Operations:

| Operation        | Time Complexity |
|------------------|-----------------|
| **Insert**       | O(log n)        |
| **Delete Min/Max** | O(log n)      |
| **Extract Min/Max** | O(log n)     |
| **Peek (Min/Max)** | O(1)          |
| **Heapify**      | O(n)            |
| **Decrease Key** | O(log n)        |
| **Merge**        | O(n log n)      |

Binary heaps offer a good balance of simplicity and efficiency for operations like insertion, extraction, and heapification, which is why they are widely used in priority queues.
