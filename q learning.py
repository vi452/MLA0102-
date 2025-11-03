# Program: Grid-World Navigation using Q-Learning
# Question 27 – AI & Expert System (MLA0102)

import random

# ----- Grid World Setup -----
ROWS = 5
COLS = 5

# Rewards:
# Goal = +10
# Obstacle = -10
# Step penalty = -1

reward_grid = [
    [0, 0, 0, 0, 0],
    [0, -10, 0, -10, 0],
    [0, 0, 0, 0, 0],
    [-10, 0, -10, 0, -10],
    [0, 0, 0, +10, 0]     # goal at (4,3)
]

start_state = (0, 0)
goal_state = (4, 3)

actions = ['up', 'down', 'left', 'right']

# ----- Q-Table Initialization -----
Q = {}
for r in range(ROWS):
    for c in range(COLS):
        Q[(r, c)] = {a: 0 for a in actions}


# ----- Helper Functions -----
def get_next_state(state, action):
    r, c = state

    if action == "up": r -= 1
    elif action == "down": r += 1
    elif action == "left": c -= 1
    elif action == "right": c += 1

    # stay in boundary
    r = max(0, min(r, ROWS - 1))
    c = max(0, min(c, COLS - 1))

    return (r, c)


def choose_action(state, epsilon):
    # ε-greedy strategy
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)
    else:
        return max(Q[state], key=Q[state].get)


# ----- Q-Learning Algorithm -----
alpha = 0.7      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.3    # exploration rate
episodes = 200

for _ in range(episodes):
    state = start_state

    while state != goal_state:
        action = choose_action(state, epsilon)
        next_state = get_next_state(state, action)
        reward = reward_grid[next_state[0]][next_state[1]]

        # Q-Learning update rule
        Q[state][action] = Q[state][action] + alpha * (reward + gamma * max(Q[next_state].values()) - Q[state][action])

        state = next_state


# ----- Optimal Path Extraction -----
state = start_state
optimal_path = [state]

while state != goal_state:
    action = max(Q[state], key=Q[state].get)
    next_state = get_next_state(state, action)

    optimal_path.append(next_state)
    state = next_state


# ----- Output -----
print("\nQ-TABLE (Final Learned Values):")
for state, values in Q.items():
    print(state, ":", values)

print("\nOptimal Path Found:")
print(" → ".join(str(i) for i in optimal_path))
