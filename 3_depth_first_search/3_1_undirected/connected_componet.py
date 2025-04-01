"""
DFS with previsit and postvisit functions
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