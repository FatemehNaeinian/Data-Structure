#!/usr/bin/env python
# coding: utf-8

# In[92]:


base_dict = {'pirahan': [['not_important'], [200000, 700000], ['sadeh']],
           'kapshen': [['meshki'], [0, 2000000], ['charm']],
           'shalvar': [['sabz', 'khakestari'], [400000, 1000000], ['katan', 'jean']],
           'joorab': [['sefid'], ['not_important'], ['nakhi']]}


# In[96]:


def check_price(lebas_price, favorite_price):
#     print(lebas_price)
#     print(favorite_price)
    if 'not_important' in favorite_price:
        return True
    if (int(lebas_price) >= favorite_price[0]) and (int(lebas_price) <= favorite_price[1]):
        return True
    else: return False
    

def check(lebas_info, favorite_info):
#     print(favorite_info[0].count(lebas_info[1]))
#     print(lebas_info)
#     print('not_important' in favorite_info[0])
    if (lebas_info[1] in favorite_info[0]) or ('not_important' in favorite_info[0]):
        
        if check_price(lebas_info[2], favorite_info[1]):
#             print('meow')
            if lebas_info[3] in favorite_info[2] or ('not_important' in favorite_info[2]):
                return True
    return False


# In[5]:


n = int(input())
lebasha = []
for i in range(n):
    lebasha.append(list(input().split()))


# In[97]:


count_dict = {'pirahan':0, 'kapshen':0, 'shalvar':0, 'joorab':0}
for lebas in lebasha:
    if lebas[0] == 'pirahan':
        if check(lebas, base_dict['pirahan']):
            count_dict['pirahan'] += 1
    if lebas[0] == 'kapshen':
        if check(lebas, base_dict['kapshen']):
            count_dict['kapshen'] += 1
    if lebas[0] == 'shalvar':
        if check(lebas, base_dict['shalvar']):
            count_dict['shalvar'] += 1
    if lebas[0] == 'joorab':
        if check(lebas, base_dict['joorab']):
            count_dict['joorab'] += 1


# In[102]:


print(count_dict['pirahan'])
print(count_dict['kapshen'])
print(count_dict['shalvar'])
print(count_dict['joorab'])


# In[ ]:




