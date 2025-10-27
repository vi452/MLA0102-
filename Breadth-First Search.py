# Breadth-First Search (BFS) in Python
from collections import deque
def bfs(graph, start):
    visited = []             
    queue = deque([start])   
    while queue:
        node = queue.popleft()   
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
print("Breadth-First Search Traversal:")
bfs(graph, start_node)

output:
A B C D E F 
