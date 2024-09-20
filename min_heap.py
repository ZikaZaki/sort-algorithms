class MinHeap:
    def __init__(self, array=None):
        self.heap = []
        if isinstance(array, list):
            self.heap = array.copy()
            self._build()

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return (2 * i) + 1

    def _right(self, i):
        return (2 * i) + 2
        
    def _build(self):
        if len(self.heap) > 1:
            for i in range(len(self.heap) // 2 - 1, -1, -1):
                self._siftdown(i)
    
    def _siftup(self, i):
        n = len(self.heap)
        if n > 1 and i < n:
            parent = self._parent(i)
            while i != 0 and self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
                parent = self._parent(i)

    # More efficient
    def _siftdown(self, i):
        while True:
            left = self._left(i)
            right = self._right(i)
            
            if left >= len(self.heap):
                break
                
            smallest = left
            
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right
                
            if self.heap[i] <= self.heap[smallest]:
                break
                
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    # More clean
    def _siftdown(self, i):
        n = len(self.heap) # size of array (heap)
        while True:
            smallest = i
            left = self._left(i)
            right = self._right(i)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
                
    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap) - 1)
        
    def update_by_index(self, i, new):
        if i < 0 or i >= len(self.heap):
            raise IndexError(f"{i} index out of bounds!")
            
        # get old value to check whether to siftup or siftdown
        old = self.heap[i]
        self.heap[i] = new
        
        if new < old:
            self._siftup(i)
        else:
            self._siftdown(i)
    
    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)
        else:
            raise ValueError(f"{old} not found in the heap!")

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        n = len(self.heap) - 1
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]
        min_val = self.heap.pop()
        self._siftdown(0)
        
        return min_val
        
    def get_min(self):
        if len(self.heap) == 0:
            return None
            
        return self.heap[0]


arr = [3,1,4,1,5,9,2,6,5,3,5]
my_heap = MinHeap(arr)
print("MinHeap after build: ", my_heap.heap)

min_val = my_heap.extract_min()
print(f"Extracted Min: {min_val}")
print("MinHeap after extraction: ", my_heap.heap)

my_heap.insert(0)
print("MinHeap after inserting 0: ", my_heap.heap)

my_heap.update(5, -1)
print("MinHeap after updating 5 to -1: ", my_heap.heap)

# Trying to update a non-existent value
try:
    my_heap.update(10, -5)
except ValueError as e:
    print(e)

