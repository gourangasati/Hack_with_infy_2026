class heap:
    def __init__(self):
        self.heap = []
    def _length(self):
        return len(self.heap)
    def repre(self):
        return str(self.heap)
    def insert(self,key,value):
        self.heap.append((key,value))
        self.shift_up(self.heap[-1])
    def peek(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        return self.heap[0]
    def extract(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        smallest = self.heap[0]
        last_ele = self.heap.pop()
        if self.heap:
            self.heap[0] = last_ele
            self.shift_down(0)
        return smallest
    def _parent(self,idx):
        return (idx+1 )//2 
    def _left(self,idx):
        return (2*idx)+1
    def _right(self,idx):
        return (2*idx)+2
    def heapify(self):
        pass
    def meld(self,otherheap):
        self.heap = self.heap + otherheap
        self.heapify
    def shift_up(self,idx):
        parent_index  = self._parent(idx)
        while parent_index and self.heap[idx][0] < self.heap[parent_index][0]:
            self.heap[idx], self.heap[parent_index] = self.heap[parent_index],self.heap[idx]
            idx = parent_index
            parent_index = self._parent(idx)
    def shift_down(self,idx):
        left = self._left(idx)
        right = self._right(idx)
        pass
            