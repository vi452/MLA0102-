# Program: Knight's Tour using Backtracking
# Question 21 – AI & Expert System (MLA0102)

N = 8   # size of the chessboard (you can change N to any value)

# Moves a knight can make (8 possible moves)
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


# Function to print the chessboard with path
def print_solution(board):
    for row in board:
        print(row)


# Backtracking function
def solve_knights_tour():
    # Create an NxN board initialized with -1 (unvisited)
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Knight starting position
    board[0][0] = 0  # start at (0,0)
    position = 1

    # Start exploring moves
    if not solve(board, 0, 0, position):
        print("No solution found")
    else:
        print("\nKnight's Tour Solution:")
        print_solution(board)


# Check if move is valid (inside board and unvisited)
def is_safe(x, y, board):
    return (x >= 0 and x < N and y >= 0 and y < N and board[x][y] == -1)


# Recursive function to explore all possible knight moves
def solve(board, curr_x, curr_y, move_i):
    if move_i == N * N:  # all squares visited
        return True

    # Try all possible knight moves
    for k in range(8):
        next_x = curr_x + move_x[k]
        next_y = curr_y + move_y[k]

        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_i  # mark move

            if solve(board, next_x, next_y, move_i + 1):
                return True

            # backtrack
            board[next_x][next_y] = -1

    return False


# ---- Main Program ----
solve_knights_tour()
