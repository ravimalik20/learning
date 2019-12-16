import heapq
import random


class MinHeap:
    def __init__(self, initial_data: list = None):
        if initial_data is None:
            self.heap = []
        else:
            self.heap = initial_data
        heapq.heapify(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


class MaxHeap:
    def __init__(self, initial_data: list = None):
        if initial_data is None:
            self.heap = []
        else:
            self.heap = initial_data
        heapq.heapify(self.heap)

    def push(self, val: int):
        val *= -1
        heapq.heappush(self.heap, val)

    def pop(self):
        val = heapq.heappop(self.heap)
        val *= -1

        return val

    def __len__(self):
        return len(self.heap)


if __name__ == "__main__":
    heap = MinHeap()

    for _ in range(20):
        heap.push(random.randint(0, 100))

    while len(heap) > 0:
        print(heap.pop(), end=' ')
    print('')

    heap = MaxHeap()

    for _ in range(20):
        heap.push(random.randint(0, 100))

    while len(heap) > 0:
        print(heap.pop(), end=' ')
    print('')

    data = [random.randint(0, 100) for _ in range(20)]
    heap = MinHeap(data)

    while len(heap) > 0:
        print(heap.pop(), end=' ')
    print('')
