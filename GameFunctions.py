# This is the start of placing a piece code (Ashna)





import os
from Board import Board


class Game_Functions(Board):
      def __init__(self):
        super().__init__()
      def printBoard(self):
        print(str(self.positions[0]) + "(00)----------------------" + str(self.positions[1]) +
          "(01)----------------------" + str(self.positions[2]) + "(02)")
        print("|                           |                           |")
        print("|                           |                           |")
        print("|                           |                           |")
        print("|       " + str(self.positions[8]) + "(08)--------------" +
            str(self.positions[9]) + "(09)--------------" + str(self.positions[10]) + "(10)     |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       |        " + str(self.positions[16]) + "(16)-----" +
            str(self.positions[17]) + "(17)-----" + str(self.positions[18]) + "(18)       |      |")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print(str(self.positions[3]) + "(03)---" + str(self.positions[11]) + "(11)----" + str(self.positions[19]) + "(19)               " +
            str(self.positions[20]) + "(20)----" + str(self.positions[12]) + "(12)---" + str(self.positions[4]) + "(04)")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print("|       |        " + str(self.positions[21]) + "(21)-----" +
            str(self.positions[22]) + "(22)-----" + str(self.positions[23]) + "(23)       |      |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       " + str(self.positions[13]) + "(13)--------------" +
            str(self.positions[14]) + "(14)--------------" + str(self.positions[15]) + "(15)     |")
        print("|                           |                           |")
        print("|                           |                           |")
        print("|                           |                           |")
        print(str(self.positions[5]) + "(05)----------------------" + str(self.positions[6]) +
            "(06)----------------------" + str(self.positions[7]) + "(07)")
        print("\n")
      
      def is_occupied(self, position):
          return self.getBoardPositions()[position] != 0
      def is_current_player(self, position):
          return self.getBoardPositions()[position] == self.getPlayerTurn()
      
      def place_piece(self, finished_turn=False):
            while(True):
                try:
                    position = int(input(f"Player {self.getPlayerTurn()}, enter a position (0-23), 24 to Load, 25 to Save, 26 to Restart, 27 to Replay or 28 to access main menu: "))
                    #This part will be replaced by buttons on the front end (GUI) side
                    #for example, load is a button on the screen and it will call the load() method
                    if position == 24:
                        self.load()
                    elif position == 25:
                        self.save()
                    elif position == 26:
                        self.new_restart_game()
                    elif position == 27:
                        self.replay()
                    elif position == 28:
                        self.start_menu()
                    elif 0 <= position <= 23 and not self.is_occupied(position):
                        self.getBoardPositions()[position] = self.getPlayerTurn()
                        self.printBoard() 
                    elif position < 0 or position > 28:
                        print("Invalid position. Try again.")
                    else:
                        print("Position already occupied. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")
            return finished_turn
      def move_piece(self):
            while(True):
                try:
                    position = int(input(f"Player {self.getPlayerTurn()}, select a piece to move (0-23), 24 to Load, 25 to Save, 26 to Restart, 27 to Replay or 28 to access main menu: "))
                    if position == 24:
                        self.load()
                    elif position == 25:
                        self.save()
                    elif position == 26:
                        self.new_restart_game()
                    elif position == 27:
                        self.replay()
                    elif position == 28:
                        self.start_menu()
                    elif self.is_occupied(position) and self.is_current_player(position):
                        move_to = int(input(f"Select where to move your piece {self.getPermissibleMoves()[position]}: "))
                        if move_to in self.getPermissibleMoves()[position] and not self.is_occupied(move_to):
                            self.getBoardPositions()[move_to] = self.getPlayerTurn()
                            self.getBoardPositions()[position] = 0
                            self.printBoard() 
                            break
                        else:
                            print("Invalid move. Try again.")
                    else:
                        print("Invalid choice. Select one of your pieces.")
                except (ValueError, KeyError):
                    print("Invalid input. Try again.")
          
          
      def remove_piece(self):
            while(True):
                try:
                    position = int(input(f"Player {self.getPlayerTurn()}, choose an opponent's piece to remove (0-23), 24 to Load, 25 to Save, 26 to Restart, 27 to Replay or 28 to access main menu: "))
                    if position == 24:
                        self.load()
                    elif position == 25:
                        self.save()
                    elif position == 26:
                        self.new_restart_game()
                    elif position == 27:
                        self.replay()
                    elif position == 28:
                        self.start_menu()
                    elif 0 <= position <= 23 and self.is_occupied(position) and not self.is_current_player(position):
                        self.getBoardPositions()[position] = 0
                        self.printBoard() 
                        print(f"Piece at position {position} removed.")
                        break
                    else:
                        print("Invalid choice. You must select an opponent's piece.")
                except ValueError:
                        print("Invalid input. Try again.")

        
      def fly_piece(self):
            while(True):
                  try:
                        position = int(input(f"Player {self.getPlayerTurn()}, select a piece to fly (0-23), 24 to Load, 25 to Save, 26 to Restart, 27 to Replay or 28 to access main menu: "))
                        if position == 24:
                              self.load()
                        elif position == 25:
                              self.save()
                        elif position == 26:
                              self.new_restart_game()
                        elif position == 27:
                              self.replay()
                        elif position == 28:
                              self.start_menu()
                        elif self.is_occupied(position) and self.is_current_player(position):
                              move_to = int(input("Select where to fly your piece (0-23): "))
                              if not self.is_occupied(move_to):
                                    self.getBoardPositions()[move_to] = self.getPlayerTurn()
                                    self.getBoardPositions()[position] = 0
                                    self.printBoard()
                                    break
                              else:
                                    print("Position already occupied. Try again.")
                        else:
                              print("Invalid choice. Select one of your pieces.")
                  except ValueError:
                        print("Invalid input. Try again.")
      def form_mill(self):
        mill_combinations = [
        [0, 1, 2], [2, 4, 7], [5, 6, 7],
        [0, 3, 5], [8, 9, 10], [10, 12, 15],
        [13, 14, 15], [8, 11, 13],
        [16, 17, 18], [18, 20, 23], [21, 22, 23],
        [16, 19, 21], [1, 9, 17], [20, 12, 4],
        [22, 14, 6], [3, 11, 19]
        ]
        newly_formed_mills = []
        for combo in mill_combinations:
            if self.getBoardPositions()[combo[0]] == self.getBoardPositions()[combo[1]] == self.getBoardPositions()[combo[2]] == self.getPlayerTurn():
                if combo not in self.getActiveMills():
                    self.getActiveMills().append(combo)
                    return True
        if newly_formed_mills:
            self.setActiveMills(self.getActiveMills() + newly_formed_mills)
            self.remove_piece()
        return False
      def check_remove_active_mill(self):
        for mill in self.getActiveMills():
            for position in mill:
                if self.getBoardPositions()[position] != self.getPlayerTurn():
                    self.getActiveMills().remove(mill)
                    break
      def is_game_over(self):
        opponent = 2 if self.getPlayerTurn() == 1 else 1
        opponent_pieces = self.getBoardPositions().count(opponent)
        return opponent_pieces <= 2
      def player_piece_count(self):
        return self.getBoardPositions().count(self.getPlayerTurn())
      def is_gridlocked(self):
        opponent = 2 if self.get_player_turn() == 1 else 1
        for position, player in enumerate(self.getBoardPositions()):
            if player == opponent:
                permissible = self.getPermissibleMoves()[position]
                if any([self.getBoardPositions()[move] == 0 for move in permissible]):
                    return False
        print(f"Player {opponent} is gridlocked and Player {self.getPlayerTurn()} wins!")
        exit()
      def start_menu(self):
        choice = input("Select: 1. New/Restart Game 2. Load Game 3. Game Type (default is 9): ")
        self.printBoard()
        if choice == '1':
            self.new_restart_game()
        elif choice == '2':
            self.load()
        elif choice == '3':
            print("Currently, only Nine Men's Morris (9) is supported.")
            self.new_restart_game()
        else:
            print("Invalid choice.")
            self.start_menu()

      def save(self):
        with open("saved_game_states.txt", "a") as file:
            file.write(','.join(map(str, self.getBoardPositions())) + "\n")
            print("Board state saved to file.")

      def load(self):
        if not os.path.exists("saved_game_states.txt"):
            print("No saved game state exists.")
            return
        with open("saved_game_states.txt", "r") as file:
            lines = file.readlines()
            if lines:
                state = list(map(int, lines[-1].strip().split(',')))
                self.setBoardPositions(state)
                print("Board state loaded from file.")
            else:
                print("No saved game state exists.")

      def replay(self):
        if not os.path.exists("saved_game_states.txt"):
            print("No saved game state exists.")
            return
        with open("saved_game_states.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                state = list(map(int, lines[-2].strip().split(',')))
                self.setBoardPositions(state)
                print("Board state set to the previous state from the file.")
            else:
                print("Not enough saved game states for replay.")


      def display(self):
        print("Board positions:", self.getBoardPositions())
        print("Player's turn:", self.getPlayerTurn())
        print("Active mills:", self.getActiveMills())
        print("Remaining turns:", self.getRemainingTurns())

      def place_a_piece_phase(self):
        while(self.getRemainingTurns() != 0):
            self.place_piece()
            if self.form_mill():
                self.remove_piece()
            self.check_remove_active_mill()
            self.setPlrTurn(2 if self.getPlayerTurn() == 1 else 1)
            self.decrementTurns()


      def move_a_piece_phase(self):
        while not self.is_game_over():
            if self.player_piece_count() == 3:
                finished_turn = self.fly_piece()
            else:
                finished_turn = self.move_piece()
            if self.form_mill():
                finished_turn = self.remove_piece()
            self.check_remove_active_mill()
            self.setPlrTurn(2 if self.getPlayerTurn() == 1 else 1)

      def new_restart_game(self):
        super().__init__
        self.play_game()

      def play_game(self):
        self.place_a_piece_phase()
        self.move_a_piece_phase()
        print(f"Player {self.getPlayerTurn()} wins!")

