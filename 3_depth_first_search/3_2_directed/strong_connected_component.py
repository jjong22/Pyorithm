"""
    Decomposition of a Graph into SCCS

At the moment of the first discovery of a node v, we assign it an integer cc identifying the connected componentents to which it belongs.
The value cc is initialized to 0 and to be incremented each time the DFS calls explore.
"""
G = list         
u, v = int, int
visited = [ False ] * u 
pre = [0] * v
post = [0] * v
scc = 0 # number of strongly connected components

# https://wondy1128.tistory.com/130
# may be usefull

# TODO:
# 1. Implement Kosaraju's algorithm