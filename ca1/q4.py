#!/usr/bin/env python
# coding: utf-8

# In[43]:


def find_len_zeros(N):
    maximum = 0
    prev = 0
    curr = -1
    for i in range(0,len(N)+1):
        if i < len(N):
            if N[i] == "1" :
                prev = curr
                curr = i
        else:
            prev = curr
            curr = i
        gap = curr - prev -1
        if gap > maximum:
            maximum = gap
    return maximum
    
# find_len_zeros('100011101100')


# In[5]:


test_case = int(input())
N = ['']*test_case
K = ['']*test_case
string = ['']*test_case
for t in range(test_case):
    N[t], K[t] = list(map(int, input().split()))
    string[t] = input()


# In[45]:


for i in range(test_case):
    zero_str = ''.join(['0']*K[i])
    maximum = 0
    for j in range(N[i]-K[i]+1):
        new_str = string[i][0:j] + zero_str + string[i][j+K[i]:]
#         print(find_len_zeros(new_str))
#         print(new_str)
        str_count = find_len_zeros(new_str)
        if str_count > maximum:
            maximum = str_count
    print(maximum)


# In[ ]:





# In[ ]:





# In[ ]:




