import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []
distance = [float("Inf")] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def check_for_negative_cycle(start):
    distance[start] = 0
    for i in range(n): # |V - 1| iter

        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != float("Inf") and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == n - 1: # negative cycle
                    return True
    return False

has_negative_cycle = check_for_negative_cycle(1)

if has_negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == float("Inf"):
            print(-1)
        else:
            print(distance[i])