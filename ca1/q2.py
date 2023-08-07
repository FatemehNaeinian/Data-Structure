#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = list(map(int, input().split()))
stones = [int(x) for x in input()]

count = [0]*10
count_for_any_index = []
for j in range(len(stones)):
    count[stones[j]] += 1
    count_for_any_index.append(count[:])
abs_sub = [9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9]

for x in range(m):
    i =  int(input())
    ans = 0
    for k in range(10):
        ans += count_for_any_index[i-1][k]*abs_sub[9-stones[i-1]+k]
    print(ans)


# In[ ]:




