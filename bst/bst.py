class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.visited = 0

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
        else:
            self._insert(self.root, value)

    def _insert(self, cur_node, value):
        if (cur_node.value <= value):
            if cur_node.right != None:
                self._insert(cur_node.right, value)
            else:
                cur_node.right = Node(value)
        else:
            if cur_node.left != None:
                self._insert(cur_node.left, value)
            else:
                cur_node.left = Node(value)

    def fromArray(self, array):
        for i in array:
            self.insert(i)

    def search(self, value):
        self.visited = 0
        r = self.root

        if (self.root == None):
            return False

        while r:
            self.visited += 1
            if r.value < value:
                r = r.right
            elif r.value > value:
                r = r.left
            else:
                return True
        return False
    
    def min(self):
        self.visited = 0
        r = self.root

        if (self.root == None):
            return None
        
        self.visited += 1
        while r.left:
            self.visited += 1
            r = r.left

        return r.value

    def max(self):
        self.visited = 0
        r = self.root
        
        if (self.root == None):
            return None

        self.visited += 1
        while r.right:
            self.visited += 1
            r = r.right

        return r.value

    def visitedNodes(self):
        return self.visited

bst1 = BinarySearchTree()

print(bst1.search(10))
print(bst1.visitedNodes())
print(bst1.min())
print(bst1.max())

print("====================")


bst2 = BinarySearchTree()
bst2.fromArray([5, 3, 1, 4, 7, 6, 8])

print(bst2.search(5))
print(bst2.visitedNodes())
print(bst2.search(7))
print(bst2.visitedNodes())
print(bst2.search(6))
print(bst2.visitedNodes())
print(bst2.search(10))
print(bst2.visitedNodes())
print("MIN: " + str(bst2.min()))
print(bst2.visitedNodes())
print("MAX: " + str(bst2.max()))
print(bst2.visitedNodes())

print("===============================================")

bst3 = BinarySearchTree()
bst3.fromArray([1, 3, 4, 5, 6, 7, 8])

print("MIN: "  + str(bst3.min()))
print(bst3.visitedNodes())
print("MAX: " + str(bst3.max()))
print(bst3.visitedNodes())