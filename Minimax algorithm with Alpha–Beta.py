import math
def minimax(depth, node, isMax, values, alpha, beta):
    if depth == 3:    
        return values[node]
    if isMax:
        best = -math.inf
        for i in range(2):
            val = minimax(depth+1, node*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha: break  
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth+1, node*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha: break 
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Best Move Value for AI (Max Player):",
      minimax(0, 0, True, values, -math.inf, math.inf))


output:
Best Move Value for AI (Max Player): 5

