'''
https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
'''

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (f'{root.info} - {root.level}', end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        self.root = self._insert(self.root, val, 0)
        return self.root
    
    def _insert(self, node, val, lvl):
        if not node:
            n = Node(val)
            n.level = lvl
            return n
        else:
            if node.info == val:
                return node
            elif node.info < val:
                node.right = self._insert(node.right, val, lvl + 1)
            else:
                node.left = self._insert(node.left, val, lvl + 1)
        return node

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
