import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
predecessor = [None] * (n+1)

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost)) 

start, end = map(int, input().split())

dist = [float('inf')] * (n+1)
dist[start] = 0

heap = [(0, start)]
while heap:
    current_cost, u = heapq.heappop(heap)
    
    if current_cost > dist[u]:
        continue
    
    for v, w in graph[u]:
        new_cost = current_cost + w
        if new_cost < dist[v]:
            dist[v] = new_cost
            predecessor[v] = u
            heapq.heappush(heap, (new_cost, v))

path = []
ptr = end
while ptr is not None:
    path.append(ptr)
    ptr = predecessor[ptr]
path.reverse()


print(dist[end])
print(len(path))
print(*path)