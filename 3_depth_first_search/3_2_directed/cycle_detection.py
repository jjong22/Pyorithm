G = list # directed graph  
u, v = int, int
visited = [ False ] * u 
pre = [0] * v
post = [0] * v
clk = 0

def previsit(v):
    global clk
    pre[v] = clk
    clk += 1
    
def postvisit(v):
    global clk
    post[v] = clk
    clk += 1
    
def explore(G, v):
    visited[v] = True
    previsit(v)
    for u in G[v]:
        if not visited[u]:
            explore(G, u)
    postvisit(v)
    
def dfs(G):
    for v in G:
        if not visited[v]:
            explore(G, v)

foward_edges = []
back_edges = []
cross_edges = []

def classify_edges(G):
    for v in G:
        for u in G[v]:
            if pre[v] < pre[u] and post[v] > post[u]:
                foward_edges.append((v, u))
            elif pre[v] > pre[u] and post[v] < post[u]:
                back_edges.append((v, u))
            elif pre[v] < pre[u] and post[v] < post[u]:
                cross_edges.append((v, u))
            else:
                pass # not happen
"""
A directed graph has a cycle iff its DFS reveals a back edge.
"""

def has_cycle(G):
    if len(back_edges) > 0:
        return True
    else:
        return False    
            