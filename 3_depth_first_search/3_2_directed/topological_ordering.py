G = list # directed acyclic graph (DAG)
u, v = int, int
visited = [ False ] * u 
pre = [ (i, -1) for i in range(v) ] # to memorize its idx
post = [ (i, -1) for i in range(v) ] 
clk = 0

def previsit(v):
    global clk
    pre[v][1] = clk
    clk += 1
    
def postvisit(v):
    global clk
    post[v][1] = clk
    clk += 1
    
def explore(G, v): 
    visited[v] = True
    previsit(v)
    for u in G[v]:
        if not visited[u]:
            explore(G, u)
    postvisit(v)
    
def dfs(G): # first v shoud be source
    for v in G:
        if not visited[v]:
            explore(G, v)

post.sort(key=lambda x: x[1]) # sort by postvisit time
topological_order = [i[0] for i in post]

"""
Given a directed acyclic graph, 
we can compute its topological ordering in O(|V|+|E|) time.

"""