'''
Hacker Rank: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
'''

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
  common_node = None
  data = {v1, v2}
  one_node = rec_find(root, data)
  if not one_node:
    return None
  data.remove(one_node[0].info)
  val_2 = data.pop()
  return find_next(one_node, val_2)

def find_next(nodes, val):
    for node in nodes:
        ret = rec_find(node, {val})
        if ret:
            return node
    return None
    
def rec_find(start, data):
    if not start:
        return None
    if start.info in data:
        return [start]
    ret = rec_find(start.left, data) or rec_find(start.right, data)
    if ret:
        ret.append(start)
    return ret

tree = BinarySearchTree()
t = int(input() or 7)

arr = list(map(int, input().split() or [5, 3, 8, 2, 4, 6, 7]))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split() or [7, 3]))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
