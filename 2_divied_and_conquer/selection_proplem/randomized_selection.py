import random

"""
Randomized Selection Algorithm
Given n elements and an integer k, we wish to find the kth smallest element.

:Input: A list S, an integer k
:Output: The kth smallest element in S

time complexity: Θ(n) on average, O(n^2) in the worst case
"""
def random_selection(S: list, k: int) -> int:
    pivot = random.choice(S)
    s_l = [i for i in S if i < pivot]
    s_r = [i for i in S if i > pivot]
    s_v = [i for i in S if i == pivot]
    
    if k <= len(s_l):
        return random_selection(s_l, k)
    elif k <= len(s_l) + len(s_v):
        return pivot
    else:
        return random_selection(s_r, k - len(s_l) - len(s_v))
        
s_list = [6,5,4,3,2,1,4,5,2,3,6,7,4,3,1]
s_list = sorted(s_list)
print(s_list)
print(random_selection(s_list, 7))