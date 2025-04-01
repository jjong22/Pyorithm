def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

"""
Closest Pair of Points
Given n points in the plane, find a pair with smallest Euclidean distance.

:Input: A list of points in 2D space
:Output: The smallest distance between any two points

time complexity: O(n log n)
T(n) = 2T(n/2) + O(n)
"""

def closest_pair(eucledian_points):
    if len(eucledian_points) <= 1:
        return 0
    if len(eucledian_points) == 2:
        return distance(eucledian_points[0], eucledian_points[1])
    if len(eucledian_points) == 3:
        return min(distance(eucledian_points[0], eucledian_points[1]), 
                   distance(eucledian_points[1], eucledian_points[2]), 
                   distance(eucledian_points[2], eucledian_points[0]))
    
    mid = len(eucledian_points) // 2
    vertical_line = eucledian_points[mid][0]  # x coordinate of the mid point
    
    delta = min(closest_pair(eucledian_points[:mid]), closest_pair(eucledian_points[mid:]))
    
    p_delta = [i for i in eucledian_points if (i[0] - vertical_line) ** 2 <= delta]
    p_delta.sort(key=lambda p: p[1]) # soting by y coordinate
    
    for i in range(len(p_delta)):
        for j in range(i + 1, min(i + 12, len(p_delta))):
            delta = min(delta, distance(p_delta[i], p_delta[j]))
            
    return delta

# return power of distance

eucledian_points = [(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22), (23,24), (25,26), (27,28), (29,30)]
eucledian_points = sorted(eucledian_points)
print(closest_pair(eucledian_points))