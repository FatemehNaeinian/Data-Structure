
import sys
sys.setrecursionlimit(10**8)
class Graph:
    def __init__(self, nodes, N):
        self.num_nodes = N 
        self.edges = {}
        self.color = {} 
        for i in nodes:
            self.edges[i] = []
            self.color[i] = 'white'
        
    def add(self, uivi):
        self.edges[uivi[0]] += [uivi[1]]
        self.edges[uivi[1]] += [uivi[0]]
        
    
    def check_possible(self, S, F, C):
        if S == F:
            print('YES')
            return
        if self.num_nodes != len(S):
            print('NO')
            return
        if len(S) != len(F) or len(S) != len(C) or len(C) != len(F):
            print('NO')
            return
        self.S = S
        self.F = F
        self.C = C
        self.collected = []
        self.K = [0]*len(C)
        self.DFS()
        
        if sum(self.collected) == 0:
            print("YES")
        else:
            print("NO")
        
    def DFS(self):
        self.Find_keys(1)  
        print('collected',self.collected)
        print('klid mojud',self.S)
        print('klid haghighi',self.F)
        print('klid tahvil dade',self.K)
        print('rang establ',self.C)
        print('\n')
        for c in self.color:
            self.color[c] = 'white'
        self.give_keys(1)
        print('collected',self.collected)
        print('klid mojud',self.S)
        print('klid haghighi',self.F)
        print('klid tahvil dade',self.K)
        print('rang establ',self.C)
        print('\n')

    def Find_keys(self, u):
        if self.S[u-1] != None:
            self.collected.append(S[u-1])
            self.S[u-1] = None
        self.color[u] = 'gray'
        for v in self.edges[u]:
            if self.color[v] == 'white' and self.C[v-1] in self.collected:
                self.Find_keys(v)
        self.color[u] = 'black'
        
    def give_keys(self, u): 
        # print('collected',self.collected)
        # print('klid mojud',self.S)
        # print('klid haghighi',self.F)
        # print('klid tahvil dade',self.K)
        # print('rang establ',self.C)
        # print('\n')
        self.color[u] = 'gray'
        for v in self.edges[u]:
            if self.color[v] == 'white' and self.C[v-1] in self.collected:
                self.give_keys(v)
        self.color[u] = 'black'
        if self.F[u-1] in self.collected and self.K[u-1] == 0:
            # print(u-1)
            # print(self.F[u-1])
            self.K[u-1] = self.F[u-1]
            self.collected.remove(self.F[u-1])
        
        
        
        
T = int(input())

for i in range(T):
    input()
    N, M = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    S = [int(x) for x in input().split()]
    F = [int(x) for x in input().split()]

    uivi = []
    nodes = []
    for j in range(M):
        ui, vi = [int(x) for x in input().split()]
        uivi.append([ui,vi])
        nodes.append(ui)
        nodes.append(vi)

    nodes = set(nodes)
    graph = Graph(nodes, N) 

    for j in range(M):
        graph.add(uivi[j])

    graph.check_possible(S, F, C)

        