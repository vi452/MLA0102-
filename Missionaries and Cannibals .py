# Q12 – Missionaries and Cannibals Problem
# Using Breadth-First Search (BFS)

from collections import deque

def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Check for invalid states
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    # Cannibals cannot outnumber missionaries on either side
    if (m_left and m_left < c_left) or (m_right and m_right < c_right):
        return False
    return True

def get_successors(state):
    m, c, boat = state
    successors = []
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible people to move
    for m_move, c_move in moves:
        if boat == 1:  # boat on left
            new_state = (m - m_move, c - c_move, 0)
        else:           # boat on right
            new_state = (m + m_move, c + c_move, 1)
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

# Run the search
path = bfs()

# Display result
print("Missionaries and Cannibals Solution Path:")
for step in path:
    print(step)
