import random

def random_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

def attacks(state):
    c = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                c += 1
    return c

def hill_climb(n):
    state = random_state(n)
    cost = attacks(state)
    while True:
        neighbors = []
        for c in range(n):
            for r in range(n):
                if r != state[c]:
                    nstate = state.copy()
                    nstate[c] = r
                    neighbors.append(nstate)
        next_state = min(neighbors, key=attacks)
        next_cost = attacks(next_state)
        if next_cost >= cost:
            return state, cost
        state, cost = next_state, next_cost

# Run for N=8
sol, cost = hill_climb(8)
print("Final Board (column=row position):", sol)
print("Final cost (attacking pairs):", cost)
