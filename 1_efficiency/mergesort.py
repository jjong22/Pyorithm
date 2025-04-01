"""
Sorts a list of numbers using the merge sort algorithm.
:Input: A list L of n integers
:Output: A list of the n integers sorted in increasing order
time complexity: O(n log n)
"""
def merge(left: list, right: list) -> list:
    result = []
    for i in range(len(left) + len(right)):
        if left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            
    return result

def mergesort(nums: list) -> list:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = mergesort(nums[:mid])
    right_half = mergesort(nums[mid:])

    return merge(left_half, right_half)