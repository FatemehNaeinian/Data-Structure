from collections import deque

n, k = list(map(int, input().split(' ')))
ai = list(map(int, input().split(' ')))
q = int(input())
q_num = []
for i in range(q):
    q_num.append(int(input()))
    
line1_k_num = deque()
line2_max_k_num = deque()
maximum_k = []

for i in range(n):
    line1_k_num.append(ai[i])
    if line2_max_k_num and line1_k_num[0] == line2_max_k_num[0] and len(line1_k_num) > k:
        line2_max_k_num.popleft()
    if len(line1_k_num) > k:
        line1_k_num.popleft()
    while line2_max_k_num and ai[i] > line2_max_k_num[-1]:
        line2_max_k_num.pop()
    line2_max_k_num.append(ai[i])
    maximum_k.append(line2_max_k_num[0])

maximum_for_r = []
for i in range(q):
    maximum_for_r.append(maximum_k[q_num[i]-1])

for i in range(q):
    print(maximum_for_r[i])