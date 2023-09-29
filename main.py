# This is the start of placing a piece code (Ashna)
def print_board(board):
    print(board[0] + "(00)----------------------" + board[1] +
          "(01)----------------------" + board[2] + "(02)")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|       " + board[8] + "(08)--------------" +
          board[9] + "(09)--------------" + board[10] + "(10)     |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + board[16] + "(16)-----" +
          board[17] + "(17)-----" + board[18] + "(18)       |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(board[3] + "(03)---" + board[11] + "(11)----" + board[19] + "(19)               " +
          board[20] + "(20)----" + board[12] + "(12)---" + board[4] + "(04)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |        " + board[21] + "(21)-----" +
          board[22] + "(22)-----" + board[23] + "(23)       |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       " + board[13] + "(13)--------------" +
          board[14] + "(14)--------------" + board[15] + "(15)     |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(board[5] + "(05)----------------------" + board[6] +
          "(06)----------------------" + board[7] + "(07)")
    print("\n")



def place_piece(board, player):
   print_board(board)
   while True:
        try:
            position = int(input(f"Player {player}, enter a position (0-23) that has not been taken: "))
            if(position > 23 or position < 0):
                raise ValueError("Invalid position. Try again.")
            board[position] = player
            break
        except ValueError as e:
            print(e)
        except (IndexError, TypeError):
            print("Invalid input. Try again")
    


# Numbers for input will be the first index, Letters for input will be the second index
board = []
for i in range(24):
    board.append('0')

player1 = '1'
player2 = '2'

for x in range(18):
    place_piece(board, player1)
    place_piece(board, player2)







