class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertionHelper(self):
        x = [15, 10, 25, 5, 13, 20, 30, 35, 3, 7, 11, 14, 18, 22, 28, 2, 4, 6, 8]
        for element in x:
            self.insertion(element)

    def insertion(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = newNode
                    break
                else:
                    current = current.left
            elif data >= current.data:
                if current.right is None:
                    current.right = newNode
                    break
                else:
                    current = current.right

    def inOrder(self):
        self.inOrderHelper(self.root)
    
    def inOrderHelper(self, current):
        if current is None:
            return
        self.inOrderHelper(current.left)
        print(current.data, "->", end=" ")
        self.inOrderHelper(current.right)

    def preOrder(self):
        self.preOrderHelper(self.root)
    
    def preOrderHelper(self, current):
        if current is None:
            return
        print(current.data, "->", end=" ")
        self.preOrderHelper(current.left)
        self.preOrderHelper(current.right)

    def postOrder(self):
        self.postOrderHelper(self.root)
    
    def postOrderHelper(self, current):
        if current is None:
            return
        self.postOrderHelper(current.left)
        self.postOrderHelper(current.right)
        print(current.data, "->", end=" ")

    def contains(self, value):
        current = self.root
        while current is not None:
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else:
                return True
        return False

    def remove(self, value):
        self.removeHelper(value, None, self.root)

    def removeHelper(self, target, parentNode, currentNode):
        while True:
            if currentNode is None:
                print("Value not found")
                return
            if target < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left
            elif target > currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is None and currentNode.right is None:
                    if parentNode is None:
                        self.root = None
                    elif parentNode.left == currentNode:
                        parentNode.left = None
                    elif parentNode.right == currentNode:
                        parentNode.right = None
                else:
                    if currentNode.right is None:
                        currentNode.data = self.findLargest(currentNode.left)
                        self.removeHelper(currentNode.data, currentNode, currentNode.left)
                    else:
                        currentNode.data = self.findSmallest(currentNode.right)
                        self.removeHelper(currentNode.data, currentNode, currentNode.right)
                return

    def findLargest(self, current):
        if current.right is None:
            return current.data
        else:
            return self.findLargest(current.right)
        
    def findSmallest(self, current):
        if current.left is None:
            return current.data
        else:
            return self.findSmallest(current.left)    

if __name__ == "__main__":
    b = BinarySearchTree()
    b.insertionHelper()
    print("inOrder [Left,Root,Right]")
    b.inOrder()
    print("\npreOrder [Root,Left,Right]")
    b.preOrder()
    print("\npostOrder [Left,Right,Root]")
    b.postOrder()
    print()
    print("\n",b.contains(2))
    b.remove(2)
    print()
    print("after deletion")
    b.inOrder()
