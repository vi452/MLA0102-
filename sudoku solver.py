# Program: Sudoku Solver using Backtracking (CSP)
# Question 26 – AI & Expert System (MLA0102)

# Check if placing num in board[row][col] is valid
def is_valid(board, row, col, num):

    # Check if num exists in same row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num exists in same column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3×3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


# Backtracking function to solve Sudoku
def solve_sudoku(board):

    for row in range(9):
        for col in range(9):

            # Find empty cell (0 means empty)
            if board[row][col] == 0:

                # Try possible numbers 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        # Undo (backtrack)
                        board[row][col] = 0

                return False  # If no number fits, backtrack

    return True  # Puzzle solved


# Print Sudoku board
def print_board(board):
    for row in board:
        print(row)


# ----- Example Sudoku Input (0 = empty cell) -----

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("\nSudoku Input:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\nNo solution exists.")
