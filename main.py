# This is the start of moving a piece code (Ashna)



def printBoard(board):
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

def make_move(board, player):
    while True:
        try:
            current_position = int(input(f"Player {player}, select a piece to move (0-23): "))
            if board[current_position] != player:
                print("Invalid choice. You must select your own piece.")
                continue
            print("Permissible moves: ", permissible_moves[current_position])
            move_to = int(input("Select where to move your piece: "))
            if move_to in permissible_moves[current_position] and board[move_to] == ' ':
                board[current_position] = ' '
                board[move_to] = player
                printBoard(board)
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError, KeyError):
            print("Invalid input. Try again.")




if __name__ == "__main__":
    player1 = 'X'
    player2 = 'X'

    board = [" " for _ in range(24)]

    # setting up board with pieces on board already (this will not happen in real life, just for this user story)
    board[0] = 'X'
    board[3] = 'O'
    board[7] = 'X'
    board[17] = 'O'
    permissible_moves = {
        0: [1, 3],
        1: [0, 2, 9],
        2: [1, 4],
        3: [0, 11, 5],
        4: [2, 12, 7],
        5: [3, 6],
        6: [5, 7, 14],
        7: [4, 6],
        8: [9, 11],
        9: [1, 8, 17, 10],
        10: [9, 12],
        11: [8, 3, 19, 13],
        12: [20, 10, 4, 15],
        13: [11, 14],
        14: [13, 22, 6, 15],
        15: [14, 12],
        16: [19, 17],
        17: [16, 18, 9],
        18: [17, 20],
        19: [16, 11, 21],
        20: [18, 12, 23],
        21: [19, 22],
        22: [14, 21, 23],
        23: [20, 22]
}


print("OG Board")
printBoard(board)

# Player 1's turn
print("Player 1's turn")
make_move(board, player1)

# Player 2's turn
print("Player 2's turn")
make_move(board, player2)




