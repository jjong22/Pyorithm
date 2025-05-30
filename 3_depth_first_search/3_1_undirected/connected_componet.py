"""
    Computing connected components

At the moment of the first discovery of a node v, we assign it an integer cc identifying the connected componentents to which it belongs.
The value cc is initialized to 0 and to be incremented each time the DFS calls explore.
"""
G = list         
u, v = int, int
visited = [ False ] * u 
pre = [0] * v
post = [0] * v
cc = 0 # number of connected components

def explore(G, v):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            explore(G, u)

def dfs(G):
    global cc
    for v in G:
        if not visited[v]:
            cc += 1
            explore(G, v)