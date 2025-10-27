# 8 Queens Problem using Backtracking
N = 8
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()
def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False
    return True
def solve(board, row=0):
    if row == N:
        print("Solution:")
        print_board(board)
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0  
    return False
board = [[0]*N for _ in range(N)]
solve(board)

output:
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .

