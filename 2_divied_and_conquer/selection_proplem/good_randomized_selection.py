import random

"""
Good Randomized Selection Algorithm
Given n elements and an integer k, we wish to find the kth smallest element.

:Input: A list S, an integer k
:Output: The kth smallest element in S

time complexity: O(n) on average with array size it at most n(3/4)^i at ith phase.
"""

def good_random_selection(S, k):
    pivot = random.choice(S)
    s_l = [i for i in S if i < pivot]
    s_r = [i for i in S if i > pivot]
    s_v = [i for i in S if i == pivot]
    
    if len(s_l) < k // 4 or len(s_r) < k // 4:
        return good_random_selection(S, k) # reselct pivot
    
    if k <= len(s_l):
        return good_random_selection(s_l, k)
    elif k <= len(s_l) + len(s_v):
        return pivot
    else:
        return good_random_selection(s_r, k - len(s_l) - len(s_v))
    
s_list = [6,5,4,3,2,1,4,5,2,3,6,7,4,3,1]
s_list = sorted(s_list)
print(s_list)
print(good_random_selection(s_list, 7))