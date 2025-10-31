# Program : A* Pathfinding Algorithm
# Question 18 – AI & Expert System (MLA0102)

from queue import PriorityQueue

# Graph definition: adjacency list with weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'F': 1, 'E': 1},
    'E': {'F': 2},
    'F': {}
}

# Heuristic values (example estimated cost to reach goal F)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 0
}

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))      # priority queue stores (cost, node)
    cost_so_far = {start: 0}
    parent = {start: None}

    print("\nNode Expansion Order:")

    while not pq.empty():
        current_cost, current_node = pq.get()
        print(current_node, end=" → ")

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node].items():
            new_cost = cost_so_far[current_node] + weight

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]    # f(n) = g(n) + h(n)
                pq.put((priority, neighbor))
                parent[neighbor] = current_node

    # Reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, cost_so_far[goal]


# ---- Main Program ----
start_node = 'A'
goal_node = 'F'

path, total_cost = a_star(start_node, goal_node)

print("\nOptimal Path Found:", " → ".join(path))
print("Total Path Cost:", total_cost)
