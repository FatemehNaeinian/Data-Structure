import heapq
T = int(input())

for i in range(T):
    N, M = list(map(int, input().split()))
    Z = list(map(int, input().split()))
    ghaltak = []
    for j in range(M):
        ghaltak.append(list(map(int, input().split())))
        
    heap = []
    for j in range(M):
        heapq.heappush(heap, [-(ghaltak[j][1]-ghaltak[j][0]+1), ghaltak[j]])
        
    # print(heap)
    ghaltak_count = 0
    win = True
    while sum(Z) != 0:
        # print(Z)
        if len(heap) == 0:
            print('Make-us-whole')
            win = False
            break
        for j in range(len(Z)):
            if (Z[j] > 0) and (heap[0][1][0]-1 <= (j)) and (heap[0][1][1]-1 >= (j)):
                Z[j] -= 1
                if Z[j] == 0:
                    for k in range(len(heap)):
                        if (heap[k][1][0]-1 <= (j)) and (heap[k][1][1]-1 >= (j)):
                            heap[k][0] += 1
                    
        heap[0][1][2] -= 1
        if heap[0][1][2] == 0:
            heapq.heappop(heap)
        heapq.heapify(heap)
        ghaltak_count += 1
        # print(heap)
        
        
    if win:
        print('Isak-is-alive', ghaltak_count)