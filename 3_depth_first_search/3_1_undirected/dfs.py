"""
Depth First Search (DFS) for undirected graphs

Input: G = (V, E) is a graph ; v is a vertex in V
Output: visited(u) is set to True for all nodes u reachable from v

time complexity: O(|V|+|E|)
"""

G = list
u, v = int, int
visited = [ False ] * u 

def explore(G, v):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            explore(G, u)
            
"""
DFS with previsit and postvisit functions
"""
G = list         
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
            