# Program: Expectiminimax Algorithm (Max, Min, Chance Nodes)
# Question 24 – AI & Expert System (MLA0102)

import random

# Expectiminimax function
def expectiminimax(node, depth, node_type):
    """
    node_type:
        "MAX"  -> maximizing player
        "MIN"  -> minimizing player
        "CHANCE" -> chance/probabilistic node
    """

    # Base case: leaf node returns a utility value
    if depth == 0 or type(node) is int:
        return node

    # MAX node: choose the highest value
    if node_type == "MAX":
        best = float('-inf')
        for child in node:
            best = max(best, expectiminimax(child, depth - 1, "MIN"))
        return best

    # MIN node: choose the lowest value
    elif node_type == "MIN":
        best = float('inf')
        for child in node:
            best = min(best, expectiminimax(child, depth - 1, "CHANCE"))
        return best

    # CHANCE node: compute expected utility (probabilities sum to 1)
    elif node_type == "CHANCE":
        probability = 1 / len(node)  # equal probability
        expected_value = 0
        for child in node:
            expected_value += probability * expectiminimax(child, depth - 1, "MAX")
        return expected_value


# ---- Game Tree Representation ----
# Structure: [Left subtree, Right subtree]
# Leaf nodes represent utilities

# MAX → MIN → CHANCE → utility values
game_tree = [
    [ [3, 5], [2, 9] ],     # Left branch of MAX
    [ [8, 4], [6, 7] ]      # Right branch of MAX
]

# ---- Main Program ----
result = expectiminimax(game_tree, depth=3, node_type="MAX")
print("Optimal Expected Utility for MAX Player:", result)
