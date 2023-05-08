"""
import sys

INF = sys.maxsize
n = 100
dist = [[INF] * n for i in range(n)]
next = [[0] * n for i in range(n)]

# prints the path chosen to find the optimal solution
def printPath(i, j):
    if i != j:
        printPath(i, next[i][j])
    print(j, end=' ')

# finds the shortest path between all pairs of vertices
def floydWarshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    
    # prints the shortest distance and the path for every pair of vertices
    for i in range(1, n+1):
        for j in range(1, n+1):           
            if i != j:
                print(f"Shortest Distance from {i} to {j}: {dist[i][j]}, Path: ", end='')
                printPath(i, j)
                print()
"""

INF = 99999

# Sample Input - adjacency matrix of a 4-node graph
dist = [[0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]]

def APSP():
    n = len(dist)
    # Initialize the distance matrix with the given adjacency matrix
    dist_matrix = dist

    # Calculate the shortest distance for all pairs using intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

    # Print the shortest distance matrix
    print("Shortest Distance Matrix:")
    for i in range(n):
        for j in range(n):
            if dist_matrix[i][j] == INF:
                print("INF", end="\t")
            else:
                print(dist_matrix[i][j], end="\t")
        print()

APSP()
