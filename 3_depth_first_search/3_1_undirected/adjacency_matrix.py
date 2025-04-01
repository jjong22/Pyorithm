""" 
adjacency matrix is a 2D array

requires O(n^2) space
check if there is an edge between u and v in O(1) time
identify all edeges incident to a vertex u in O(n^2) time
"""

def add_edge(u, v):
    adjacency_matrix[u][v] = 1
    adjacency_matrix[v][u] = 1

n = int(input()) # number of vertices
m = int(input()) # number of edges

adjacency_matrix = [ [0]*n for i in range(n) ]

for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)