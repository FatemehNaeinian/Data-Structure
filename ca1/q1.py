#!/usr/bin/env python
# coding: utf-8

# In[16]:


def sort_by_score(names, scores):
    sorted_scores, sorted_names = zip(*sorted(zip(scores, names), reverse=True))
    return sorted_scores, sorted_names

def sort_by_name(names):
    sorted_names = sorted(names)
    return sorted_names

n, x = map(int, input().split())
names = input().split(',')
scores = list(map(int, input().split(',')))
# n, x = [10, 1]
# names = ['hooda','hamed','taj','pouya','ahmad','misagh','saman','mosi','sina','arthus']
# scores = [345,123,784,2423,434,47,67,84,62334,430]
size = - (-len(scores) * x) // 100
new_score, new_name = sort_by_score(names, scores)
new_name2 = sort_by_name(new_name[size:])
last_names = list(new_name[:size]) + new_name2
print(*last_names)

