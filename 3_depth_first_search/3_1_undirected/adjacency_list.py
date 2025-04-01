"""
adjacency list is a dictionary

requires O(|V|+|E|) space
checks in O(min(deg(u), deg(v))) time if there is an edge between u and v
identifies all edges incident to a vertex u in O(|V|+|E|) time
"""

def add_edge(u, v):
    if u not in adjacency_list:
        adjacency_list[u] = []
    if v not in adjacency_list:
        adjacency_list[v] = []
        
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

n = int(input()) # number of vertices
m = int(input()) # number of edges

adjacency_list = {}

for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)