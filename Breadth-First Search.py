# Breadth-First Search (BFS) in Python

from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = []             # List to keep track of visited nodes
    queue = deque([start])   # Initialize queue with the start node

    while queue:
        node = queue.popleft()   # Remove first element from queue
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Define graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node
start_node = 'A'

print("Breadth-First Search Traversal:")
bfs(graph, start_node)