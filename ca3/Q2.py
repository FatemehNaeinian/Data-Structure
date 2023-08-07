import heapq
n, q= list(map(int,input().split()))
numbers = list(map(int,input().split()))
for i in range(q):
    numbers.append(int(input()))

min_heap = [] 
max_heap = []
median = []
for new_number in numbers:
    if not max_heap or new_number < -max_heap[0]:
        heapq.heappush(max_heap, -new_number) 
        
    else:
        heapq.heappush(min_heap, new_number)
         
    if len(min_heap) - len(max_heap) > 1:
        temp = -heapq.heappop(min_heap)
        heapq.heappush(max_heap, temp)
    elif len(max_heap) - len(min_heap) > 1:
        temp = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, temp)
        
    if len(min_heap) > len(max_heap):
        median.append(min_heap[0])
    else:
        median.append(-max_heap[0])
    
for i in range(q):
    print(median[len(median)-q+i])
    