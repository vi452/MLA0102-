# Program : Travelling Salesman Problem (TSP)
# Question 19 – AI & Expert System (MLA0102)

from itertools import permutations

# Distance matrix (change values based on problem input)
# Cities: 0 - A, 1 - B, 2 - C, 3 - D
distance = [
    [0, 10, 15, 20],   # A -> A,B,C,D
    [10, 0, 35, 25],   # B -> A,B,C,D
    [15, 35, 0, 30],   # C -> A,B,C,D
    [20, 25, 30, 0]    # D -> A,B,C,D
]

num_cities = len(distance)
cities = list(range(num_cities))  # [0,1,2,3]

min_cost = float('inf')
best_path = None

# Check every possible route (permutations)
for perm in permutations(cities):
    cost = 0

    # cost from start to last city in order
    for i in range(num_cities - 1):
        cost += distance[perm[i]][perm[i + 1]]

    # return back to starting city
    cost += distance[perm[-1]][perm[0]]

    if cost < min_cost:
        min_cost = cost
        best_path = perm

# Print result
print("\nBest Route:", " → ".join(chr(65 + city) for city in best_path))
print("Minimum Cost:", min_cost)
