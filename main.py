# This is the start of flying a piece code (Ashna)
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 21)

def place_piece(board, player):
    while True:
        try:
            position = input(f"Player {player}, enter the row and column (such as A1): ").strip().upper()
            row, col = position[0], int(position[1]) - 1
            if not('A' <= row <= 'G') or not (0 <= col <= 6) or board[ord(row) - ord('A')][col] != ' ':
                raise ValueError("Invalid position. Try again.")
            board[ord(row) - ord('A')][col] = player
            break
        except ValueError as e:
            print(e)
        except (IndexError, TypeError):
            print("Invalid input format. Use the format 'A1'.")

board = [[' ' for _ in range(7)] for _ in range(7)]

player1 = 'X'
player2 = 'O'
players = [player1, player2]

for _ in range(18):
    current_player = players[_ % 2]
    print_board(board)
    place_piece(board, current_player)

