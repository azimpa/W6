class Minheap:
    def __init__(self):
        self.min_heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return (i * 2) + 2

    def insert(self, element):
        self.min_heap.append(element)
        self.shift_up(len(self.min_heap) - 1)

    def shift_up(self, current_idx):
        parent_idx = self.parent(current_idx)
        while current_idx > 0 and self.min_heap[parent_idx] > self.min_heap[current_idx]:
            self.min_heap[parent_idx], self.min_heap[current_idx] = self.min_heap[current_idx], self.min_heap[parent_idx]
            current_idx = parent_idx
            parent_idx = self.parent(current_idx)

    def remove(self):
        if not self.min_heap:
            return None
        self.min_heap[0] = self.min_heap[-1]
        self.min_heap.pop()
        self.shift_down(0)

    def shift_down(self, current_idx):
        end_idx = len(self.min_heap) - 1
        left_child_idx = self.left_child(current_idx)
        while left_child_idx <= end_idx:
            right_child_idx = self.right_child(current_idx)
            smallest_idx = current_idx
            if right_child_idx <= end_idx and self.min_heap[right_child_idx] < self.min_heap[smallest_idx]:
                smallest_idx = right_child_idx
            if left_child_idx <= end_idx and self.min_heap[left_child_idx] < self.min_heap[smallest_idx]:
                smallest_idx = left_child_idx

            if smallest_idx == current_idx:
                return

            self.min_heap[current_idx], self.min_heap[smallest_idx] = self.min_heap[smallest_idx],self.min_heap[current_idx]

            current_idx = smallest_idx
            left_child_idx = self.left_child(current_idx)

    def display(self):
        for element in self.min_heap:
            print(element, "|", end=" ")

if __name__ == "__main__":
    a = [70, 60, 40, 10, 20, 30, 50]
    x = Minheap()
    for element in a:
        x.insert(element)
    x.display()
    print()
    x.remove()
    print("after removal")
    x.display()