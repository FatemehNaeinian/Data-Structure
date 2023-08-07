import sys
sys.setrecursionlimit(10**5)
class Graph:
    def __init__(self, nodes):
        self.edges = {}
        self.color = {} 
        for i in nodes:
            self.edges[i] = []
            self.color[i] = 'white'
        self.d = {}
        self.f = {}
        self.time = 0
        self.edge_counter = 0
        
    def add(self, uivi):
        self.edges[uivi[0]] += [uivi[1]]
        self.edges[uivi[1]] += [uivi[0]]
        
    
    def check_possible(self):
        possible = self.DFS()
        if possible == 0:
            print("NO")
        else:
            print("YES")
        
    def DFS(self):
        self.time = 0
        for u in self.edges:
            if self.color[u] == 'white':
                self.edge_counter = 0
                self.DFS_visit(u)  
                if self.edge_counter < self.f[u] - self.d[u]:
                    return 0
        return 1
    
    def DFS_visit(self, u): 
        self.time += 1
        self.d[u] = self.time
        self.color[u] = 'gray'
        for v in self.edges[u]:
            self.edge_counter += 1
            if self.color[v] == 'white':
                self.DFS_visit(v)
        self.time += 1
        self.f[u] = self.time
        self.color[u] = 'black'
        
t = int(input())   
for _ in range(t):   
    N, M = [int(x) for x in input().split()]

    uivi = []
    for j in range(M):
        ui, vi = [int(x) for x in input().split()]
        uivi.append([ui,vi])

    nodes = range(1,N+1)
    graph = Graph(nodes)

    for j in range(M):
        graph.add(uivi[j])

    graph.check_possible()

        