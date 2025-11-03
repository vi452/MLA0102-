# Program: Travelling Salesman Problem using Ant Colony Optimization (ACO)
# Question 28 – AI & Expert System (MLA0102)

import random
import math

# ----------- Problem Setup (Distance Matrix) -------------
# Cities: A, B, C, D   (4 cities example)
distance = [
    [0, 10, 12, 11],   # A -> A,B,C,D
    [10, 0, 13,  5],   # B -> A,B,C,D
    [12, 13, 0,  3],   # C -> A,B,C,D
    [11,  5,  3, 0]    # D -> A,B,C,D
]

num_cities = len(distance)
num_ants = 6
iterations = 15

alpha = 1         # importance of pheromone
beta = 2          # importance of visibility
evaporation = 0.5 # pheromone evaporation rate
Q = 100           # pheromone strength

# Pheromone matrix (initially equal everywhere)
pheromone = [[1 for _ in range(num_cities)] for _ in range(num_cities)]


# ----------- Helper Functions ---------------

def probability(current_city, unvisited, pheromone, distance):
    probs = []
    for next_city in unvisited:
        pher = pheromone[current_city][next_city] ** alpha
        vis = (1 / distance[current_city][next_city]) ** beta
        probs.append(pher * vis)
    total = sum(probs)
    return [p / total for p in probs]


def select_next_city(current_city, unvisited):
    probs = probability(current_city, unvisited, pheromone, distance)
    return random.choices(unvisited, weights=probs)[0]


def route_length(route):
    length = 0
    for i in range(len(route) - 1):
        length += distance[route[i]][route[i + 1]]
    length += distance[route[-1]][route[0]]  # return to start
    return length


# ----------- ACO Algorithm ------------------

best_route = None
best_cost = float("inf")

for iteration in range(iterations):

    all_routes = []

    for ant in range(num_ants):

        start = random.randint(0, num_cities - 1)
        route = [start]
        unvisited = list(range(num_cities))
        unvisited.remove(start)

        while unvisited:
            next_city = select_next_city(route[-1], unvisited)
            route.append(next_city)
            unvisited.remove(next_city)

        cost = route_length(route)
        all_routes.append((route, cost))

        if cost < best_cost:
            best_cost = cost
            best_route = route

    # ---- Pheromone Update ----
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1 - evaporation)

    for route, cost in all_routes:
        for i in range(len(route) - 1):
            pheromone[route[i]][route[i + 1]] += Q / cost
        pheromone[route[-1]][route[0]] += Q / cost  # return to start

    print(f"Iteration {iteration + 1}: Best Cost = {best_cost}")

# ----------- Final Output -----------

print("\nBest Route Found by ACO:")
print(" → ".join(chr(65 + city) for city in best_route))  # convert 0,1,2,3 to A,B,C,D
print("Total Cost:", best_cost)
