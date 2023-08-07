import sys
sys.setrecursionlimit(10**6)
class Graph:
    def __init__(self, nodes):
        self.edges = {}
        self.color = {} 
        self.parent = {}
        for i in nodes:
            self.edges[i] = []
            self.color[i] = 'white'
            self.parent[i] = [1]
        self.summation = 0
        
            
    def add(self, uivi, wi):
        self.edges[uivi[0]] += [[uivi[1], wi]]
        self.edges[uivi[1]] += [[uivi[0], wi]]
        
    def calculate(self, n):
        for i in range(n):
            for j in range(i+1, n):
                self.DFS(i+1, j+1)
        return self.summation
        
        
    def DFS(self, u, v):
        for c in self.color:
            self.color[c] = 'white'
        self.DFS_visit(u, v, [])    
    
    def DFS_visit(self, u, v, path):
        if u==v:
            return
        # print(u,v)
        self.color[u] = 'gray'
        for ver, weight in self.edges[u]:
            if self.color[ver] == 'white':
                path.append(weight)
                if ver == v:
                    # print(path)
                    self.summation += sum(path)
                    return
                
                self.DFS_visit(ver, v, path)
        path.pop()
        # print(path)
        self.color[u] = 'black'
        


n = int(input())
uv = []
w = []
nodes = []
for i in range(n-1):
    ui, vi, wi = [int(x) for x in input().split()]
    uv.append([ui, vi])
    nodes.append(ui)
    nodes.append(vi)
    w.append(wi)
    
nodes = set(nodes)
graph = Graph(nodes)

for j in range(n-1):
    graph.add(uv[j],w[j])

summation = graph.calculate(n)
print(summation)