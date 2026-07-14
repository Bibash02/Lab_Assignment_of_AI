
import math

board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    [' ', ' ', ' ']
]

def print_board(board):
    for row in board:
        print(row)

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
    # rows
    for row in board:
        if row[0] == 'X':
            return 10
        elif row[0] == 'O':
            return -10
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
        
        if board[0][0] == board[1][1] == board[2][2]:
            if board [0][0] == 'X':
                return 10
            elif board [0][0] == 'O':
                return -10
        
        if board[0][2] == board[1][1] == board[2][0]:
            if board [0][2] == 'X':
                return 10
            elif board [0][0] == 'O':
                return -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth +1, True))
                    board[i][j] = ' '
        return best
    
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

print("Curren Board: ")
print_board(board)
best_move = find_best_move(board)
print("Best move for X: ", best_move)


# Minimax
# Minimax is used in two-player games. It assumes one player tries to maximize the score and the other tries to minimize it.