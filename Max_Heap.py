class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return (i * 2) + 2

    def insert(self, element):
        self.max_heap.append(element)
        self.shift_up(len(self.max_heap) - 1)

    def shift_up(self, current_idx):
        parent_idx = self.parent(current_idx)
        while current_idx > 0 and self.max_heap[parent_idx] < self.max_heap[current_idx]:
            self.max_heap[parent_idx], self.max_heap[current_idx] = self.max_heap[current_idx], self.max_heap[parent_idx]
            current_idx = parent_idx
            parent_idx = self.parent(current_idx)

    def remove(self):
        if not self.max_heap:
            return None
        self.max_heap[0] = self.max_heap[-1]
        self.max_heap.pop()
        self.shift_down(0)

    def shift_down(self, current_idx):
        end_idx = len(self.max_heap) - 1
        left_child_idx = self.left_child(current_idx)
        while left_child_idx <= end_idx:
            right_child_idx = self.right_child(current_idx)
            largest_idx = current_idx
            if right_child_idx <= end_idx and self.max_heap[right_child_idx] > self.max_heap[largest_idx]:
                largest_idx = right_child_idx
            if left_child_idx <= end_idx and self.max_heap[left_child_idx] > self.max_heap[largest_idx]:
                largest_idx = left_child_idx

            if largest_idx == current_idx:
                return

            self.max_heap[current_idx], self.max_heap[largest_idx] = self.max_heap[largest_idx], self.max_heap[current_idx]

            current_idx = largest_idx
            left_child_idx = self.left_child(current_idx)

    def display(self):
        for element in self.max_heap:
            print(element, "|", end=" ")

if __name__ == "__main__":
    a = [70, 60, 40, 10, 20, 30, 50]
    x = MaxHeap()
    for element in a:
        x.insert(element)
    x.display()
    print()
    x.remove()
    print("after removal")
    x.display()
