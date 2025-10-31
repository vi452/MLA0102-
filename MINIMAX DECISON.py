# Program : Minimax Algorithm for a Perfect Binary Tree
# Question 17 – AI & Expert System (MLA0102)

# Minimax function
def minimax(depth, nodeIndex, isMaximizingPlayer, values, maxDepth):

    # If we reach the leaf node, return the value from array
    if depth == maxDepth:
        return values[nodeIndex]

    if isMaximizingPlayer:
        # Maximizing player chooses the MAX of the two children
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, maxDepth)
        )
    else:
        # Minimizing player chooses the MIN of the two children
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, maxDepth)
        )


# ---- Main Program ----
# Leaf values (final state scores) – change as per your tree figure
values = [3, 5, 6, 9]

# Total depth: Since 4 leaves => depth = log2(4) = 2
maxDepth = 2

optimalValue = minimax(0, 0, True, values, maxDepth)

print("Leaf Node Values:", values)
print("Optimal Move for Maximizing Player:", optimalValue)
