"""
This is a deterministic selection algorithm that finds the k-th smallest element in an unsorted list.
It is based on the idea of selecting a good pivot to partition the list into smaller sublists.

:Input: A list S, an integer k
:Output: The kth smallest element in S

Time complexity: O(n) in the worst case
T(n) = O(n) + T(n/5) + T(7n/10)
"""

def deterministic_selection(s_list, k):
    if len(s_list) <= 5:
        s_list.sort()
        return s_list[k]
    
    chunks = [s_list[i:i + 5] for i in range(0, len(s_list), 5)]
    medians = [deterministic_selection(chunk, len(chunk) // 2) for chunk in chunks]

    pivot = deterministic_selection(medians, len(medians) // 2)
    
    s_l = [i for i in s_list if i < pivot]
    s_r = [i for i in s_list if i > pivot]
    s_v = [i for i in s_list if i == pivot]
    
    if k <= len(s_l):
        return deterministic_selection(s_l, k)
    elif k <= len(s_l) + len(s_v):
        return pivot
    else:
        return deterministic_selection(s_r, k - len(s_l) - len(s_v))
    
s_list = [6,5,4,3,2,1,4,5,2,3,6,7,4,3,1]
s_list = sorted(s_list)
print(s_list)
print(deterministic_selection(s_list, 7))