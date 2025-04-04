import heapq

def prim(graph, start):
    n = len(graph)
    visited = set()
    min_heap = [(0, start, None)]
    total_cost = 0
    mst = []

    while min_heap:
        cost, u, parent = heapq.heappop(min_heap)

        if u in visited:
            continue
        
        visited.add(u)
        
        if parent is not None:
            mst.append((parent, u, cost))
        
        total_cost += cost

        for v, cost in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (cost, v, u))

    return total_cost, mst

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 3), ('D', 2)],
    'C': [('A', 4), ('B', 3), ('D', 5)],
    'D': [('B', 2), ('C', 5)]
}

# Prim 알고리즘 실행
total_cost, mst = prim(graph, 'A')
print("MST:", mst)
print("Total cost:", total_cost)
