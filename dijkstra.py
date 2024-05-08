INF = 9999999
V = 5

G = [
    [0, 4, 1, 2, 0],
    [4, 0, 0, 10, 0],
    [1, 0, 0, 6, 0],
    [2, 10, 6, 0, 3],
    [0, 0, 0, 3, 0]
]

dist = [INF] * V
visited = [False] * V

# Source vertex is assumed to be 0
source = 0
dist[source] = 0

for _ in range(V - 1):
    # Find vertex with the minimum distance
    min_dist = INF
    min_vertex = -1
    for i in range(V):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_vertex = i
    
    # Mark the selected vertex as visited
    visited[min_vertex] = True
    
    # Update distances of adjacent vertices
    for i in range(V):
        if not visited[i] and G[min_vertex][i] and dist[min_vertex] + G[min_vertex][i] < dist[i]:
            dist[i] = dist[min_vertex] + G[min_vertex][i]

# Print the minimum distances
print("Vertex   Distance from Source")
for i in range(V):
    print(f"{i}\t   {dist[i]}")
