# Program : Scheduling using Simulated Annealing
# Question 20 – AI & Expert System (MLA0102)

import random
import math

# --- Problem Setup ---
tasks = ["T1", "T2", "T3", "T4", "T5", "T6"]     # 6 tasks
time_slots = [1, 2, 3]                          # 3 available time slots

# Cost function: penalizes conflicts (tasks assigned to same slot)
def calculate_cost(schedule):
    cost = 0
    for slot in time_slots:
        tasks_in_slot = schedule.count(slot)
        if tasks_in_slot > 1:
            cost += (tasks_in_slot - 1)         # penalty for same slot conflict
    return cost


# Generate a random schedule
def random_schedule():
    return [random.choice(time_slots) for _ in tasks]


# --- Simulated Annealing ---
def simulated_annealing():

    temperature = 100      # Starting temperature
    cooling_rate = 0.90    # Cooling factor
    min_temperature = 1    # Stopping point

    current_solution = random_schedule()
    current_cost = calculate_cost(current_solution)

    best_solution = current_solution[:]
    best_cost = current_cost

    print("Initial Schedule:", current_solution, "Cost:", current_cost)

    while temperature > min_temperature:

        # Create a neighboring solution
        new_solution = current_solution[:]
        index = random.randint(0, len(tasks) - 1)
        new_solution[index] = random.choice(time_slots)

        new_cost = calculate_cost(new_solution)

        # If better, take solution; if worse, accept with probability
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost

        # Update best solution
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost

        # Reduce temperature gradually
        temperature *= cooling_rate

    print("\nBest Schedule Found:")
    for t, slot in zip(tasks, best_solution):
        print(f"{t} → Slot {slot}")

    print("Final Cost:", best_cost)


# ---- Main ----
simulated_annealing()
