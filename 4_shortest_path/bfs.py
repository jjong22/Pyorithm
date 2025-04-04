from collections import deque

G = list         
u, v = int, int
visited = [ False ] * u 
dist = [float("Inf")] * u

def bfs(G, start):
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in G[node]:
            if dist[neighbor] == float("Inf"):
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
                
print(dist)