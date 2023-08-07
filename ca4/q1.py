def DFS(graph, j, S, F, C, K, collected):
    print('collected',collected)
    print('klid mojud',S)
    print('klid haghighi',F)
    print('klid tahvil dade',K)
    print('rang establ',C)
    print(j)
    print('\n')
    global possible
    global all_key
    if sum(collected) == sum(F):
        all_key = 1
    if S[j-1] != None:
        collected.append(S[j-1])
        S[j-1] = None

    temp = 0
    for i in graph[j]:
        if C[i-1] in collected and S[i-1] != None :
            temp += 1
            DFS(graph, i, S, F, C, K, collected)
        elif C[i-1] in collected and all_key == 1 and K[i-1] == 0 :
            temp += 1
            DFS(graph, i, S, F, C, K, collected)

    print("ddddd")
    if all_key == 1 :
        if F[j-1] in collected and K[j-1] == 0:
            print(j-1)
            print(F[j-1])
            K[j-1] = F[j-1]
            collected.remove(F[j-1])
    if K == F:
        possible = 1
        return
    if temp == 0 and 1 in graph[j]:
        DFS(graph, 1, S, F, C, K, collected)

T = int(input())

for i in range(T):
    input()
    graph = dict()
    M, N = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    S = [int(x) for x in input().split()]
    F = [int(x) for x in input().split()]
    for j in range(M):
        graph[j+1] = []
    for j in range(N):
        ui, vi = [int(x) for x in input().split()]
        graph[ui] += [vi]
        graph[vi] += [ui]
    possible = 0
    all_key = 0
    collected = []
    K = [0]*N
    DFS(graph, 1, S, F, C, K, collected)
    # print(graph[1])
    
    if possible == 1:
        print('YES')
    else:
        print("NO")

