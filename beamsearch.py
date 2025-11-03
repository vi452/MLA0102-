# Program: Beam Search (Pathfinding)
# Question 25 – AI & Expert System (MLA0102)

from queue import PriorityQueue

# ----------- Graph Representation (Nodes + Weighted Edges) ----------- #
graph = {
    'A': {'B': 4, 'C': 2, 'D': 7},
    'B': {'E': 5, 'F': 12},
    'C': {'G': 8, 'H': 4},
    'D': {'I': 6},
    'E': {'J': 3},
    'F': {},
    'G': {},
    'H': {'K': 5},
    'I': {},
    'J': {},
    'K': {}
}

# Heuristic function (Estimated distance to Goal K)
heuristic = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7,
    'E': 4, 'F': 15, 'G': 9, 'H': 3,
    'I': 11, 'J': 2, 'K': 0
}

beam_width = 2   # Keep only the best 2 nodes at each depth level


# ----------- Beam Search Function ----------- #
def beam_search(start, goal):
    current_level = [start]
    parent = {start: None}

    print("\nBeam Search Pathfinding")
    print("-" * 40)

    while current_level:
        print("Current Level:", current_level)

        if goal in current_level:
            break

        pq = PriorityQueue()
        next_level = []

        # Expand each node and insert children into priority queue
        for node in current_level:
            for child in graph[node].keys():
                pq.put((heuristic[child], child))   # sorting by heuristic
                parent[child] = node

        # Select only best k nodes for next level
        for _ in range(min(beam_width, pq.qsize())):
            next_level.append(pq.get()[1])

        current_level = next_level

    if goal not in parent:
        return None  # no path found

    # Reconstruct path from goal backwards
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


# ----------- Main Program ----------- #
start = 'A'
goal = 'K'

path = beam_search(start, goal)

if path:
    print("\n✅ Path Found:", " → ".join(path))
else:
    print("\n❌ No path found.")
