class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def heapify_up(self, index):
        parent = (index - 1) // 2

        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self,index):
        lchild = (index * 2) + 1
        rchild = (index * 2) + 2
        largest = index

        if lchild < len(self.heap) and self.heap[largest] > self.heap[lchild]:
            largest = lchild
        if rchild < len(self.heap) and self.heap[largest] > self.heap[rchild]:
            largest = rchild

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            return self.heapify_down(largest)
        
    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    
    def remove(self, data):
        index = self.heap.index(data)

        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]

        del self.heap[-1]

        self.heapify_down(index)




class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def heapify_up(self, index):
        parent = (index - 1) // 2

        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        lchild = (index * 2) + 1
        rchild = (index * 2) + 2
        largest = index

        if lchild < len(self.heap) and self.heap[lchild] > self.heap[largest]:
            largest = lchild
        if rchild < len(self.heap) and self.heap[rchild] > self.heap[largest]:
            largest = rchild

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    
    def remove(self, data):
        index = self.heap.index(data)

        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
        del self.heap[-1]
        self.heapify_down(index)
        