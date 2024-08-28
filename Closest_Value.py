class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findClosestValue(root, target):
    closest = float('inf')  # Initialize closest to positive infinity
    current = root

    while current is not None:
        if abs(current.data - target) < abs(closest - target):
            closest = current.data

        if target < current.data:
            current = current.left
        elif target > current.data:
            current = current.right
        else:
            # If the current node's value is equal to the target,
            # then it is the closest possible value
            return current.data

    return closest
# Create a binary search tree
root = Node(30)
root.left = Node(20)
root.right = Node(45)
root.left.left = Node(18)
root.left.right = Node(28)
root.right.left = Node(40)
root.right.right = Node(53)
root.right.right.left = Node(49)
root.right.right.right = Node(55)

target = 31
closest_value = findClosestValue(root, target)
print(f"Closest value to {target} is {closest_value}")
