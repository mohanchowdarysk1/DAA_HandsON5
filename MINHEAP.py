class MINHEAP:
    def __init__(self, key=lambda x: x):
        self.heap = []
        self.key = key

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def build_min_heap(self, array):
        self.heap = array[:]
        n = len(array)
        for i in range(n // 2, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i
        if left < len(self.heap) and self.key(self.heap[left]) < self.key(self.heap[i]):
            smallest = left
        if right < len(self.heap) and self.key(self.heap[right]) < self.key(self.heap[smallest]):
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def get_root(self):
        if not self.heap:
            return None
        return self.heap[0]

    def pop_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.min_heapify(0)
        return root


# Example usage
if __name__ == "__main__":
    # Example with integers
    heap = MINHEAP()
    heap.build_min_heap([4, 10, 3, 5, 1])
    print("Heap: ", heap.heap)
    print("Root: ", heap.get_root())
    print("Popped Root: ", heap.pop_root())
    print("Heap after Popping Root: ", heap.heap)

    # Example with custom key function (e.g., sorting by the length of strings)
    heap_strings = MINHEAP(key=len)
    heap_strings.build_min_heap(["Apple", "Banana", "Orange", "Kiwi", "Grape"])
    print("\nHeap (Strings): ", heap_strings.heap)
    print("Root (Strings): ", heap_strings.get_root())
    print("Popped Root (Strings): ", heap_strings.pop_root())
    print("Heap after popping root (Strings): ", heap_strings.heap)


