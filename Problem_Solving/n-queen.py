
N = 4

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve_nq_util(board, col):
    if col >= N:
        return True
    
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_nq_util(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_nqueen():
    board = [[ 0 for _ in range(N)] for _ in range(N)]

    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return
    
    print("Solution for", N, "-Queen:")
    print_board(board)

solve_nqueen()

# N-Queen
# N-Queen places N queens on an N×N chessboard so that no two queens attack each other.