'''
https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

class Tree:
    def __init__(self):
        self.nodes = dict()
        
    def add_edges(self, n1, n2):
        n_one = self.nodes.get(n1, Node(n1))
        n_two = self.nodes.get(n2, Node(n2))
        n_one.add(n_two)
        n_two.add(n_one)
        self.nodes[n1] = n_one
        self.nodes[n2] = n_two
        
class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.neighbors = set()
    
    def add(self, n):
        self.neighbors.add(n)

def get_dist(start, end):
    q = [(start,0, set())]
    while q:
        n,l,w = q.pop(0)
        if n.data == end.data:
            return l
        for c in n.neighbors - w:
            q.append((c,l+1, w|{c}))
    return 0
    
    #if start.data == end.data:
    #    yield working
    #for item in (start.neighbors - working):
    #    yield from get_dist(item, end, working | {item})
                        
def do_work(tree, q):
    lq = len(q)
    if lq < 2:
        return 0
    u_v = 0
    for x in range(lq-1):
        item1 = tree.nodes.get(q[x])
        if not item1:
            return 0
        for y in range(x+1,lq):
            item2 = tree.nodes.get(q[y])
            if not item2:
                return 0
            u_v += (item1.data * item2.data * get_dist(item1, item2))
    return u_v % (10**9+7)

if __name__ == '__main__':
    n, q = [int(x) for x in input().split()]
    tree = Tree()
    for _ in range(n-1):
        a, b = [int(x) for x in input().split()]
        tree.add_edges(a,b)
    for _ in range(q):
        input()
        print(do_work(tree, [int(i) for i in input().split()]))
        