
colors = ['Red', 'Green', 'Blue']
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

def is_safe(node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def color_map(node_list, assignment={}):
    if len(assignment) == len(node_list):
        return assignment
    node = node_list[len(assignment)]
    for color in colors:
        if is_safe(node, color, assignment):
            assignment[node] = color
            result = color_map(node_list, assignment)
            if result:
                return result
            del assignment[node]
    return None

nodes = list(graph.keys())
solution = color_map(nodes)

print("Map Coloring Solution:")
for region, color in solution.items():
    print(region, "→", color)


output:
    Map Coloring Solution:
A → Red
B → Green
C → Blue
D → Red



