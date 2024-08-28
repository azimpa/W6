class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    def inorderTraversal(node):
        nonlocal prev, is_bst
        if node is None:
            return
    
        inorderTraversal(node.left)

        if prev is not None and prev.data >= node.data:
            is_bst = False

        prev = node

        inorderTraversal(node.right)

    prev = None
    is_bst = True

    inorderTraversal(root)

    return is_bst

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

is_bst = isBST(root)
print("Is the given tree a BST?", is_bst)
