class MinHeap:
    def __init__(self, array=None):
        self.heap = []
        if isinstance(array, list) and array:
            self.heapify(array)
    
    @property
    def is_empty(self):
        """Returns True if the heap is empty, False otherwise."""
        return len(self.heap) == 0
    
    @property    
    def size(self):
        """Returns the size of the heap."""
        return len(self.heap)
        
    def __parent(self, i):
        """Returns the parent node of (i) node"""
        return (i - 1) // 2
        
    def __left(self, i):
        """Returns the left child of (i) node"""
        return (2 * i) + 1
        
    def __right(self, i):
        """Returns the right child of (i) node"""
        return (2 * i) + 2
    
    def __siftdown(self, i):
        """Moves element at index (i) down to maintain the heap property."""
        n = self.size
        
        while True:
            smallest = i
            left = self.__left(i)
            right = self.__right(i)
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
                
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            if smallest == i:
                break
            
            # Swap current element with the smallest child
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            
    def __siftup(self, i):
        """Moves element at index (i) up to maintain the heap property."""
        parent = self.__parent(i)
        
        while i > 0 and self.heap[parent] > self.heap[i]:
            # Swap the current element with its parent
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.__parent(i)
    
    def __build(self):
        """Builds the min-heap following the bottom-up approach"""
        n = self.size
        
        if n > 1:
            # Starting from the last non-leaf node
            for i in range(n // 2 - 1, -1, -1):
                self.__siftdown(i)
        
    def heapify(self, array):
        """Converts an arbitrary list into a heap."""
        self.heap = array.copy()
        self.__build()

    def push(self, element):
        """Inserts an element into the heap and maintains the heap property."""
        self.heap.append(element)
        self.__siftup(self.size - 1)
        
    def pop(self):
        """Removes and returns the smallest element from the heap."""
        if self.is_empty:
            raise IndexError("Heap is empty!")
        
        if self.size == 1:
            return self.heap.pop()

        # Swap the first element (min) with the last, then remove the last
        min_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.size > 1:
            self.__siftdown(0)
        
        return min_element
    
    def replace(self, element):
        """Removes the smallest element and inserts a new element."""
        if self.is_empty:
            raise IndexError("Heap is empty!")
        
        min_element = self.heap[0]
        self.heap[0] = element
        # Always sift down to maintain heap property
        self.__siftdown(0) 
        
        return min_element

    def update(self, i, new_element):
        if i < 0 or i >= self.size:
            raise IndexError("Invalid index!")
        
        old_element = self.heap[i]
        self.heap[i] = new_element
        if new_element < old_element:
            self.__siftup(i)
        else:
            self.__siftdown(i)
        
    
    def merge(self, other_heap):
        """Merges another MinHeap with the current one."""
        if not isinstance(other_heap, MinHeap):
            raise TypeError(f"Expected {other_heap} to be an instance of MinHeap!")
            
        self.heap.extend(other_heap.heap)
        self.__build()
            
    def min(self):
        """Returns the smallest (minimum) element without removing it."""
        if self.is_empty:
            raise IndexError("Heap is empty!")
        
        return self.heap[0]
    
    def peek_n(self, n):
        """Returns the n smallest elements from the heap without modifying it."""
        if n < 1 or n > self.size:
            raise IndexError("Invalid index!")
        
        return sorted(self.heap)[:n]
        
    def clear(self):
        """Clears the heap."""
        self.heap.clear()
    
    def __iter__(self):
        """Returns an iterator for the heap."""
        return iter(self.heap)
    

# Example usage
min_heap = MinHeap()
min_heap.push(3)
min_heap.push(1)
min_heap.push(4)
min_heap.push(1)
min_heap.push(5)
min_heap.push(9)
min_heap.push(2)
min_heap.push(6)
min_heap.push(5)
min_heap.push(3)
min_heap.push(5)

print("Min-heap:", min_heap.heap)
print("Get min element:", min_heap.min())
print("Pop min element:", min_heap.pop())
print("Heap after min pop:", min_heap.heap)
min_heap.update(1, 5)
print("Heap after update:", min_heap.heap)
