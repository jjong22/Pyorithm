"""
Binary Search Algorithm
Find a key k in a large file containing keys z[0, 1, ..., n-1] in sorted order
:Input: A sorted list L of n integers
:Output: The index of k in L | -1 if k is not present

time complexity: O(log n)
T(n) = T(n/2) + O(1)
"""

def binary_search(sorted_arr: list, key: int) -> int:
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_arr[mid] == key:
            return mid
        elif sorted_arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1