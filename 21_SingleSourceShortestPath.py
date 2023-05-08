import networkx as nx
import matplotlib.pyplot as plt
import math


def sssp(cost, v):
    n = len(cost)
    dist = [cost[v][i] for i in range(n)]
    flag = [False for i in range(n)]

    flag[v] = True
    dist[v] = 0

    for j in range(1, n - 1):
        u = v
        for i in range(n):
            if flag[u] or (dist[i] < dist[u] and not flag[i]):
                u = i
        flag[u] = True
        for w in range(n):
            if cost[u][w] != math.inf and not flag[w]:
                dist[w] = min(dist[w], dist[u] + cost[u][w])

    return dist


n = 5
# Creates a 5x5 matrix, and fills it with "infinity"
adj_matrix = [[math.inf for i in range(n)] for i in range(n)]

# Adds edges and their weights/costs to the adjacency matrix
adj_matrix[0][1] = 2
adj_matrix[0][3] = 5
adj_matrix[0][4] = 2
adj_matrix[1][2] = 3
adj_matrix[3][2] = 6
adj_matrix[4][3] = 1

v = 0
dist = sssp(adj_matrix, 0)

print(dist)

labels = {}
for i in range(n):
    # Generates A, B, C, D, E
    labels[i] = (chr(ord("A") + i))

for i in range(n):
    print(f"Minimum distance from {labels[v]} to {labels[i]} is {dist[i]}")

edge_list = []
for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] != math.inf:
            edge_list.append((i, j, {'weight': adj_matrix[i][j]}))

G = nx.DiGraph(edge_list)
edge_labels = nx.get_edge_attributes(G, "weight")

pos = nx.spring_layout(G, seed=5)
nx.draw_networkx(G, pos, node_color="lightblue", node_size=1500, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
