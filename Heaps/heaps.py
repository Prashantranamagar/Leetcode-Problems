"""
Heaps

It is a complte binary tree
But the mumbers are not distributed in the same way as in binary tree
In heaps each node has a number that is higher than that of all of its  decendents
another difference in a heap from binary tree is that the heaps can have duplicates
heaps are not good fro searching 
good for trackin the largest item on  the top
max heap --> you have the highest value at the top root node
min heap --> where you have the lowest value at the top root node


used in Priority Queue


Time Complexity for both insert and romove is O(logn) for heap
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] >self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[index]):
                max_index = left_index
            
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index  = max_index
            else:
                return
            



    def remove(self):
        """
        Removes and returns the maximum value from the heap.
        Edge Cases: when the heap is empty , when the heap has only one element, when the heap has more than one element
        """

        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value_ = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value_

heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)

print(heap.heap)