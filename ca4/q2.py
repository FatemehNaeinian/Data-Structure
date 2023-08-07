import sys
sys.setrecursionlimit(10**6)
class Graph:
    def __init__(self, nodes):
        self.edges = {}
        self.color = {} 
        for i in nodes:
            self.edges[i] = []
            self.color[i] = 'white'
            
    def add(self, uivi):
        self.edges[uivi[0]] += [uivi[1]]
        self.edges[uivi[1]] += [uivi[0]]
        
    def delete(self, ui):
        self.edges.pop(ui, None)
        self.color.pop(ui, None)
        for key in self.edges:
            if ui in self.edges[key]:
                self.edges[key].remove(ui)
    
    def check_connected(self):
        sub = self.DFS()
        if sub > 1:
            print("NO")
        else:
            print("YES")
        
    def DFS(self):
        sub = 0
        for c in self.color:
            self.color[c] = 'white'
        for u in self.edges:
            if self.color[u] == 'white':
                sub += 1
                if sub < 2:
                    self.DFS_visit(u)    
        return sub
    
    def DFS_visit(self, u):
        self.color[u] = 'gray'
        for v in self.edges[u]:
            if self.color[v] == 'white':
                self.DFS_visit(v)
        self.color[u] = 'black'
        
    
N, M = [int(x) for x in input().split()]

uivi = []
nodes = []
for j in range(M):
    ui, vi = [int(x) for x in input().split()]
    uivi.append([ui,vi])
    nodes.append(ui)
    nodes.append(vi)

nodes = set(nodes)
graph = Graph(nodes)

for j in range(M):
    graph.add(uivi[j])

graph.check_connected()
for j in range(N):
    c = int(input())
    if j < N-1:
        graph.delete(c)
        graph.check_connected()
    