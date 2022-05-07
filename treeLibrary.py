import random

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class treeLibrary:
    def __init__(self, n):
        self.N = n
        self.t = None

    def createTree(self, n, node):
        if n > self.N:
            return
        randomNumber = random.randint(1, 4)
        if randomNumber == 1:
            return 
        elif randomNumber == 2:
            n = n + 1
            node.left = Node(n)
            self.createTree(n, node.left)
        elif randomNumber == 3:
            n = n + 1
            node.right = Node(n)
            self.createTree(n, node.right)
        else:
            n = n + 1
            node.left = Node(n)
            self.createTree(n, node.left)
            n = n + 1
            node.right = Node(n)
            self.createTree(n, node.right)

t = treeLibrary(10)
tree = Node(1)
t.createTree(1, tree)

