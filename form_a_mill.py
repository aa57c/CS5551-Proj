class Board:
    def __init__(self):
        self.__positions = [0] * 24
        self.__player_turn = 1
        self.__active_mills = []
        self.__remaining_turns = 18
        self.__permissible_moves = {
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

class Game_Functions(Board):
    def __init__(self):
        super().__init__()
    def printBoard(self):
        board = [' ' if piece == 0 else '1' if piece == 1 else '2' for piece in self.get_positions()]
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

    def form_mill(self):
        mill_combinations = [
        [0, 1, 2], [2, 4, 7], [5, 6, 7],
        [0, 3, 5], [8, 9, 10], [10, 12, 15],
        [13, 14, 15], [8, 11, 13],
        [16, 17, 18], [18, 20, 23], [21, 22, 23],
        [16, 19, 21], [1, 9, 17], [20, 12, 4],
        [22, 14, 6], [3, 11, 19]
        ]
        for combo in mill_combinations:
            if self.get_positions()[combo[0]] == self.get_positions()[combo[1]] == self.get_positions()[combo[2]] == self.get_player_turn():
                if combo not in self.get_active_mills():
                    self.get_active_mills().append(combo)
                    return True
        return False

def main():
    game = Game_Functions()
    game.start_menu()

if __name__ == "__main__":
    main()