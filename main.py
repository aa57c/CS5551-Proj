# This is the start of moving a piece code (Ashna)



def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 21)

def is_valid_move(board, start, end):
    x1, y1 = start
    x2, y2 = end

    if board[x1][y1] != 'X':
        return False
    if board[x2][y2] != ' ':
        return False
    
    if abs(x1 - x2) + abs(y1 - y2) != 1:
        return False
    
    return True

def make_move(board, start, end, player):
    if is_valid_move(board, start, end):
        x1, y1 = start
        x2, y2 = end
        board[x1][y1] = ' '
        board[x2][y2] = player
        return True
    return False

player1 = 'X'
player2 = 'O'

board = [
    [' ' for _ in range(7)] for _ in range(7)
]

print("OG Board")
print_board(board)

# Player 1's turn
print("Player 1's turn")
start = (3, 3)
end = (3, 2)
make_move(board, start, end, player1)
print_board(board)

# Player 2's turn
print("Player 2's turn")
start = (1, 1)
end = (1, 2)
make_move(board, start, end, player2)
print_board(board)




