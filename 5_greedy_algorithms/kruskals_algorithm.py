import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
# may be implement with disjoint set!
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
edges = []
total_cost = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort() # sorted with cost

for i in range(m):
    cost, a, b = edges[i]
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost
        
# parent will be a MST
print(total_cost)