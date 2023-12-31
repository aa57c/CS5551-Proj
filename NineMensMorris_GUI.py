import os
import pickle
import sys
import time
import pygame
from NineMensMorris_Game import Game
# Global Variables

# DEBUG - purposes for DEBUGGING
DEBUG = False
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



# Define some paths for images
CURRENT_DIR = os.path.dirname(__file__)

BOARD_IMG_PATH = os.path.join(CURRENT_DIR, 'assets\\boardImgs\\')
MODE_BTN_PATH = os.path.join(CURRENT_DIR, 'assets\\modeBtns\\')
PLAYER_BTN_PATH = os.path.join(CURRENT_DIR, 'assets\\playerPieces\\')
SIDE_BTN_PATH = os.path.join(CURRENT_DIR, 'assets\\sideBtns\\')
REPLAY_BTN_PATH = os.path.join(CURRENT_DIR, 'assets\\replayBtns\\')
TEMP_LOG_PATH = 'temp_log.pkl'
LOAD_VAR_PATH = 'load_game.txt'
# Initialize pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 18)

# Set up the screen
screen = pygame.display.set_mode((600, 750))
pygame.display.set_caption("Nine Men Morris")

# Load board images
boardImg3 = pygame.transform.scale(pygame.image.load(BOARD_IMG_PATH + '3mens.png'), (500, 500))
boardImg6 = pygame.transform.scale(pygame.image.load(BOARD_IMG_PATH + '6mens.png'), (500, 500))
boardImg9 = pygame.transform.scale(pygame.image.load(BOARD_IMG_PATH + 'dragon9mens.png'), (500, 500))

# Load avatar images
pantherimg = pygame.transform.scale(pygame.image.load(PLAYER_BTN_PATH + 'panther.png'), (30, 30))
dragonimg = pygame.transform.scale(pygame.image.load(PLAYER_BTN_PATH + 'dragon.png'), (30, 30))

# Load buttons and adjust sizes

play_button = pygame.transform.scale(pygame.image.load(REPLAY_BTN_PATH + 'play_button.png'), (30, 30))
pause_button = pygame.transform.scale(pygame.image.load(REPLAY_BTN_PATH + 'pause_button.png'), (30, 30))
rewind_button = pygame.transform.scale(pygame.image.load(REPLAY_BTN_PATH +'rewind_button.png'), (30, 30))
fast_forward_button = pygame.transform.scale(pygame.image.load(REPLAY_BTN_PATH +'fast_forward_button.png'), (30, 30))
back_button = pygame.transform.scale(pygame.image.load(REPLAY_BTN_PATH +'back_button.png'), (30, 30))

restart_button = pygame.transform.scale(pygame.image.load(SIDE_BTN_PATH +'restart.png'), (30, 30))
replay_button = pygame.transform.scale(pygame.image.load(SIDE_BTN_PATH + 'replay_button.png'), (30, 30))
save_button = pygame.transform.scale(pygame.image.load(SIDE_BTN_PATH + 'save_button.png'), (30, 30))
load_button = pygame.transform.scale(pygame.image.load(SIDE_BTN_PATH + 'load_button.png'), (30, 30))
# Game mode selection buttons
human_v_comp = pygame.transform.scale(pygame.image.load(MODE_BTN_PATH + 'robo1.png'), (30, 30))
human_v_human = pygame.transform.scale(pygame.image.load(MODE_BTN_PATH + 'multi_player.png'), (30, 30))





class GUI_State():
    def __init__(self):
        # all game state data members
        self.board = Game
        # coordinates of all the button positions on the board including replay, save, load, and restart buttons
        self.coords = {}
        # game loop variables (different game states)
        self.is_load = False
        self.is_in_game_mode_selection = False
        self.is_in_sleep = False
        self.is_in_play = False
        self.is_in_replay = False
        self.is_paused = False
        self.is_gameover = False
        self.can_removepiece = False
        self.is_running = True
        # all other data members
        # the current position of the piece the player picked
        self.startpos = -1
        # the position the player wants to move or fly to
        self.endpos = -1

        # Board image
        self.boardImg = pygame.Surface

        # counter for replay/play loop
        self.counter = 0.0

        # replay/play state loop variables
        self.replay_state = 0
        self.play_loop = 0
        self.play_length = 0

        # coordinates for the buttons in replay state
        self.replay_coords = {}
        # coordinates for the buttons in play state
        self.play_coords = {}
        # coordinates for the buttons in game mode selection state
        self.selection_coords = {}

        # clickables for the coordinates on the board during game, replay, play states
        self.selection_clickables = []
        self.play_clickables = []
        self.replay_clickables = [] 
        self.clickables = []
    

    # Setters

    def set_current_log_GUI(self, current_log_GUI):
        self.current_log_GUI = current_log_GUI
    
    def set_clickables(self, clickables: list):
        self.clickables = clickables
    
    def set_selection_clickables(self, selection_clickables: list):
        self.selection_clickables = selection_clickables

    def set_play_clickables(self, play_clickables: list):
        self.play_clickables = play_clickables

    def set_replay_clickables(self, replay_clickables: list):
        self.replay_clickables = replay_clickables

    def set_selection_coords(self, selection_coords: dict):
        self.selection_coords = selection_coords

    def set_play_coords(self, play_coords: dict):
        self.play_coords = play_coords
    def set_replay_coords(self, replay_coords: dict):
        self.replay_coords = replay_coords
    
    def set_board(self, board: Game):
        self.board = board

    def set_coords(self, coords: dict):
        self.coords = coords

    def set_is_load(self, is_load: bool):
        self.is_load = is_load
    def set_is_running(self, is_running: bool):
        self.is_running = is_running

    def set_is_in_game_mode_selection(self, is_in_game_mode_selection: bool):
        self.is_in_game_mode_selection = is_in_game_mode_selection

    def set_is_in_sleep(self, is_in_sleep: bool):
        self.is_in_sleep = is_in_sleep
    
    def set_is_in_play(self, is_in_play: bool):
        self.is_in_play = is_in_play
    
    def set_is_in_replay(self, is_in_replay: bool):
        self.is_in_replay = is_in_replay
    
    def set_is_paused(self, is_paused: bool):
        self.is_paused = is_paused

    def set_is_gameover(self, is_gameover: bool):
        self.is_gameover = is_gameover

    def set_can_removepiece(self, can_removepiece: bool):
        self.can_removepiece = can_removepiece

    def set_startpos(self, startpos: int):
        self.startpos = startpos

    def set_endpos(self, endpos: int):
        self.endpos = endpos

    def set_play_length(self, play_length: int):
        self.play_length = play_length

    def set_boardImg(self):
        # setting the board image in the window (will change depending on the board size)
        if(self.get_board().get_board_size() == 3):
            self.boardImg = boardImg3
        elif(self.get_board().get_board_size() == 6):
            self.boardImg = boardImg6
        elif(self.get_board().get_board_size() == 9):
            self.boardImg = boardImg9
        else:
            raise Exception("Incorrect board size. Board image could not be set")

    def set_counter(self, counter: float):
        self.counter = counter
    def set_replay_state(self, replay_state: int):
        self.replay_state = replay_state
    def set_play_loop(self, play_loop: int):
        self.play_loop = play_loop

    # Getters
    def get_current_log_GUI(self):
        return self.current_log_GUI
    def get_clickables(self):
        return self.clickables
    def get_selection_clickables(self):
        return self.selection_clickables
    def get_play_clickables(self):
        return self.play_clickables
    def get_replay_clickables(self):
        return self.replay_clickables
    def get_selection_coords(self):
        return self.selection_coords
    def get_play_coords(self):
        return self.play_coords
    def get_replay_coords(self):
        return self.replay_coords
    
    def get_coords(self):
        return self.coords
    
    def get_board(self):
        return self.board

    def get_is_load(self):
        return self.is_load
    
    def get_is_running(self):
        return self.is_running

    def get_is_in_game_mode_selection(self):
        return self.is_in_game_mode_selection

    def get_is_in_sleep(self):
        return self.is_in_sleep

    def get_is_in_play(self):
        return self.is_in_play

    def get_is_in_replay(self):
        return self.is_in_replay

    def get_is_paused(self):
        return self.is_paused

    def get_is_gameover(self):
        return self.is_gameover

    def get_can_removepiece(self):
        return self.can_removepiece
    
    def get_startpos(self):
        return self.startpos

    def get_endpos(self):
        return self.endpos

    def get_play_length(self):
        return self.play_length

    def get_boardImg(self):
        return self.boardImg

    def get_counter(self):
        return self.counter

    def get_replay_state(self):
        return self.replay_state

    def get_play_loop(self):
        return self.play_loop 
    
    # gets the coordinates for replay, save, load, and restart from extracting from the main coordinates attribute 
    def get_replay_restart_btn_coords(self):
        if self.get_board().get_board_size() == 3:
            return self.get_coords()[9], self.get_coords()[10], self.get_coords()[11], self.get_coords()[12]
        elif self.get_board().get_board_size() == 6:
            return self.get_coords()[16], self.get_coords()[17], self.get_coords()[18], self.get_coords()[19]
        elif self.get_board().get_board_size() == 9:
            return self.get_coords()[24], self.get_coords()[25], self.get_coords()[26], self.get_coords()[27]
    
    def setup_coords_for_replay_play_selection_clickables(self):
        replay_coords = {
            1: (22, 550),  # rewind a move button
            2: (169, 550), # play button
            3: (450, 550), # fast forward button
            4: (550, 550), # back button
        }
        play_coords = {
            1: (169, 550),  # play button
            2: (308, 550), # pause button
            3: (550, 550), # back button
        }
        selection_coords = {
            1: (22, 550),  # single player
            2: (169, 550), # multiplayer
        }
        self.set_replay_coords(replay_coords)
        self.set_play_coords(play_coords)
        self.set_selection_coords(selection_coords)


        self.set_replay_clickables([pygame.Rect(c[0], c[1], 30, 30) for c in self.get_replay_coords().values()])
        self.set_play_clickables([pygame.Rect(c[0], c[1], 30, 30) for c in self.get_play_coords().values()])
        self.set_selection_clickables([pygame.Rect(c[0], c[1], 30, 30) for c in self.get_selection_coords().values()])


        

    def setup_coords_for_clickables(self):
        if(self.get_board().get_board_size() == 9):
            self.set_coords({
                0: (22, 22), # positions 0-23 are the 24 positions on the board
                1: (230, 22),
                2: (450, 22),
                3: (22, 240),
                4: (450, 240),
                5: (22, 450),
                6: (230, 450),
                7: (450, 450),
                8: (95, 95),
                9: (230, 95),
                10: (380, 95),
                11: (95, 240),
                12: (380, 240),
                13: (95, 378),
                14: (230, 378),
                15: (380, 378),
                16: (162, 169),
                17: (230, 169),
                18: (308, 169),
                19: (162, 240),
                20: (308, 240),
                21: (162, 308),
                22: (230, 308),
                23: (308, 308),
                24: (550,22), # replay button
                25: (550, 122), # save button
                26: (550, 222), # load button
                27: (550, 322) # restart button
            })
        elif(self.get_board().get_board_size() == 6):
            self.set_coords({
                0: (12, 16),
                1: (235, 16),
                2: (460, 16),
                3: (125, 130),
                4: (235, 130),
                5: (348, 130),
                6: (12, 240),
                7: (125, 240),
                8: (348, 240),
                9: (460, 240),
                10: (125, 350),
                11: (235, 350),
                12: (348, 350),
                13: (12, 463),
                14: (235, 463),
                15: (460, 463),
                16: (550, 22), # replay button
                17: (550, 122), # save button
                18: (550, 222), # load button
                19: (550, 322) # restart button
            })
        elif(self.get_board().get_board_size() == 3):
            self.set_coords({
                0: (33, 34),
                1: (238, 34),
                2: (443, 34),
                3: (33, 240),
                4: (238, 240),
                5: (445, 240),
                6: (33, 443),
                7: (238, 443),
                8: (445, 443),
                9: (550, 22), # replay button
                10: (550, 122), # save button
                11: (550, 222), # load button
                12: (550, 322) # restart button
            })
        else:
            raise Exception("Something went wrong when establishing coordinates for clickables")
        self.set_clickables([pygame.Rect(c[0], c[1], 30, 30) for c in self.get_coords().values()])
        # DEBUG print("Clickables: ", self.get_clickables())
    

    
    # DEBUG Making sure board is being set properly inside the class
    '''
        def printBoardProperties(self):
        print(f"Board Size: {self.get_board().get_board_size()}")
        print(f"Positions: {self.get_board().get_positions()}")
        print(f"Player Turn: {self.get_board().get_player_turn()}")
        print(f"Remaining Turns: {self.get_board().get_remaining_turns()}")
        print(f"Permissible Moves: {self.get_board().get_permissible_moves()}")
    
    '''

    
    
    
    # Functions to draw the game state
    def draw_board(self):
        try:
            if not self.get_is_in_game_mode_selection():
                # Draw the background board
                screen.blit(self.get_boardImg().convert(), (0, 0))

                # Draw borders around the clickable areas
                if DEBUG and not (self.get_is_in_replay() and self.get_is_in_play()):
                    clickables_to_draw = self.get_replay_clickables() if self.get_is_in_replay() else self.get_clickables()
                    for rect in clickables_to_draw:
                        pygame.draw.rect(screen, BLACK, rect, 1)

                # Draw the pieces on the board
                for pos, value in enumerate(self.get_board().get_positions()):
                    x, y = self.get_coords()[pos]
                    piece_img = None
                    if value == 1:
                        piece_img = pantherimg.convert_alpha()
                        screen.blit(piece_img, (x, y))
                    elif value == 2:
                        piece_img = dragonimg.convert_alpha()
                        screen.blit(piece_img, (x, y))

                # Highlight selected piece with a green rectangle
                if self.get_startpos() > -1:
                    x, y = self.get_coords()[self.get_startpos()]
                    pygame.draw.rect(screen, GREEN, (x, y, 30, 30), 3)
            else:
                return

        except Exception as e:
            print(f"Error drawing the board: {e}")
    
    def draw_buttons(self):

        # These buttons will be drawn if the game state is neither in replay or play mode
        if not (self.get_is_in_replay() or self.get_is_in_play() or self.get_is_in_game_mode_selection()):
            replay_button_coord, save_button_coord, load_button_coord, restart_button_coord = self.get_replay_restart_btn_coords()

            screen.blit(replay_button.convert_alpha(), replay_button_coord)
            screen.blit(save_button.convert_alpha(), save_button_coord)
            screen.blit(load_button.convert_alpha(), load_button_coord)
            screen.blit(restart_button.convert_alpha(), restart_button_coord)
        # These buttons will be drawn if the game state is in replay but not in play mode
        elif self.get_is_in_replay() and not self.get_is_in_play():
            rewind_button_coord = self.get_replay_coords()[1]
            play_button_coord = self.get_replay_coords()[2]
            fast_forward_button_coord = self.get_replay_coords()[3]
            back_button_coord = self.get_replay_coords()[4]
            screen.blit(rewind_button.convert_alpha(), rewind_button_coord)
            screen.blit(play_button.convert_alpha(), play_button_coord)
            screen.blit(fast_forward_button.convert_alpha(), fast_forward_button_coord)
            screen.blit(back_button.convert_alpha(), back_button_coord)
        
        # These buttons will be draw if the game state is in replay and play mode
        elif self.get_is_in_replay() and self.get_is_in_play():

            play_button_coord = self.get_play_coords()[1]
            pause_button_coord = self.get_play_coords()[2]
            back_button_coord = self.get_play_coords()[3]

            screen.blit(play_button.convert_alpha(), play_button_coord)
            screen.blit(pause_button.convert_alpha(), pause_button_coord)
            screen.blit(back_button.convert_alpha(), back_button_coord)

        # Draw the selection buttons for game mode when game is in game selection mode state
        elif self.get_is_in_game_mode_selection() and not (self.get_is_in_replay() or self.get_is_in_play()):
            human_v_comp_coord = self.get_selection_coords()[1]
            human_v_human_coord = self.get_selection_coords()[2]
            screen.blit(human_v_comp.convert_alpha(), human_v_comp_coord)
            screen.blit(human_v_human.convert_alpha(), human_v_human_coord)
    
    def draw_game_info(self):
        texts = []
        gridlocked = self.get_board().is_gridlocked()
        enemy_bot = "ENEMY BOT"

        # These statements will print on the window when the game is over
        if self.get_is_gameover():
            # replay is available even when the game is over
            if self.get_is_in_replay():
                texts = ["In Replay Mode"]
            # if not replay, then these statements will be printed if the either player is gridlocked
            elif gridlocked:
                if self.get_board().get_game_mode() == 0: # human v human game

                    texts = [
                        f"Player {1 if self.get_board().get_player_turn() == 1 else 2} is gridlocked! Player {2 if self.get_board().get_player_turn() == 2 else 1} wins!",
                        "Close window to change game settings or click Restart"
                    ]
                elif self.get_board().get_game_mode() == 1: # human v computer game
                    texts = [
                        f"Game Over! Player {1 if self.get_board().get_player_turn() == 1 else enemy_bot} wins!",
                        "Close window to change game settings or click Restart"
                    ]
            # otherwise, these statements will be printed whenever the game is over 
            else:
                if self.get_board().get_game_mode() == 0: # human v human game
                    texts = [
                        f"Game Over! Player {1 if self.get_board().get_player_turn() == 1 else 2} wins!",
                        "Close window to change game settings or click Restart"
                    ]
                elif self.get_board().get_game_mode() == 1: # human v computer game
                    texts = [
                        f"Game Over! Player {1 if self.get_board().get_player_turn() == 1 else enemy_bot} wins!",
                        "Close window to change game settings or click Restart"
                    ]
        # These statements will print when the game is not over or if it is not in game selection mode
        elif not (self.get_is_gameover() or self.get_is_in_game_mode_selection()):
            # During the place piece phase
            if self.get_board().get_remaining_turns() != 0:
                # if the player forms a mill and can remove a piece, these statements will be printed
                if self.get_can_removepiece():
                    texts = [
                        f"Player {1 if self.get_board().get_player_turn() == 1 else 2} formed a mill!",
                        "Select an opponent's piece to remove from the board."
                    ]
                # Otherwise, if game state is in replay mode, these statements will be printed
                elif self.get_is_in_replay():
                    texts = ["In Replay Mode"]
                # Otherwise, these statements will be printed, which prints who turn it is and how many total turns are left
                else:
                    if self.get_board().get_game_mode() == 0:
                        texts = [
                            f"It's Player {1 if self.get_board().get_player_turn() == 1 else 2}'s turn!",
                            f"Remaining Turns: {self.get_board().get_remaining_turns()}"
                        ]
                    elif self.get_board().get_game_mode() == 1:
                        texts = [
                            f"It's Player {1 if self.get_board().get_player_turn() == 1 else enemy_bot}'s turn!",
                            f"Remaining Turns: {self.get_board().get_remaining_turns()}"
                        ]

            # During move/fly piece phase
            elif self.get_board().get_remaining_turns() == 0:
                # If the player forms a mill and can remove a piece, these statements will be printed
                if self.get_can_removepiece():
                    texts = [
                        f"Player {1 if self.get_board().get_player_turn() == 1 else 2} formed a mill!",
                        "Select an opponent's piece to remove from the board."
                    ]
                # Otherwise, if game state is in replay mode, these statements will be printed
                elif self.get_is_in_replay():
                    texts = ["In Replay Mode"]
                # If the player has only 3 pieces and the game is 9 mens or 6 mens, then these statements will be printed
                elif self.get_board().player_piece_count() == 3 and (self.get_board().get_board_size() == 9 or self.get_board().get_board_size() == 6):
                    texts = [
                        f"It's Player {1 if self.get_board().get_player_turn() == 1 else 2}'s turn!",
                        "Select a piece to fly then select the position you want to fly to."
                    ]
                # Otherwise, these statements will be printed, which prints who turn it is and how many total turns are left
                else:
                    texts = [
                        f"It's Player {1 if self.get_board().get_player_turn() == 1 else 2}'s turn!",
                        "Select a piece to move then select the position you want to move to."
                    ]
        # When game is in select game mode state, these statements will be printed
        elif self.get_is_in_game_mode_selection():
            texts = ["Select Game Mode"]
        
        # Draw the text on screen
        for i, text in enumerate(texts):
            textsurface = myfont.render(text, False, BLACK)
            screen.blit(textsurface, (10, 600 + i * 30))
    
    # Method that handles the main game "events" (on MOUSE UP BUTTON)
    def handle_mouse_up_events(self, 
                               event):
        try:
            # if the game is in replay, go through the replay clickables
            if self.get_is_in_replay():
                print("Game is in replay mode")
                for i, rect in enumerate(self.get_replay_clickables()):
                    if rect.collidepoint(event.pos):
                        self.handle_replay_click(i)
                        break
            else:
                # otherwise go through the clickable positions on the board
                print("Game is commencing...")
                for i, rect in enumerate(self.get_clickables()):
                    if rect.collidepoint(event.pos):
                        print("Player clicked on the board...")
                        self.handle_main_game_click(i)
                        break
        except Exception as e:
            print(f"Error handling mouse up events: {e}")
    
    '''
    handles all the clicks for replay, save, load, and restart
    Depending on the size of the board, the position of where the button is will change hence the different values being compard to
    clicked_pos
    '''

    def handle_side_btn_click(self, clicked_pos):
        if self.get_board().get_board_size() == 9:
            # Replay
            if clicked_pos == 24:
                self.set_is_in_replay(True)
                self.set_current_log_GUI(self.get_current_state_and_log())
            # Save
            elif(clicked_pos == 25):
                self.get_board().save()
            # Load
            elif(clicked_pos == 26):
                self.set_is_load(True)
            # Restart
            elif(clicked_pos == 27):
                self.get_board().new_restart_game()
                self.set_is_gameover(False)
            else:
                print("Did not click side (replay, save, load, restart) buttons")
        elif(self.get_board().get_board_size() == 6):
            # Replay
            if(clicked_pos == 16):
                self.set_is_in_replay(True)
                self.set_current_log_GUI(self.get_current_state_and_log())
            # Save
            elif(clicked_pos == 17):
                self.get_board().save()
            # Load
            elif(clicked_pos == 18):
                self.set_is_load(True)
            # Restart
            elif(clicked_pos == 19):
                self.get_board().new_restart_game()
                self.set_is_gameover(False)
            else:
                print("Did not click side (replay, save, load, restart) buttons")
        elif(self.get_board().get_board_size() == 3):
            # Replay
            if(clicked_pos == 9):
                self.set_is_in_replay(True)
                self.set_current_log_GUI(self.get_current_state_and_log())
            # Save
            elif(clicked_pos == 10):
                self.get_board().save()
            # Load
            elif(clicked_pos == 11):
                self.set_is_load(True)
            # Restart
            elif(clicked_pos == 12):
                self.get_board().new_restart_game()
                self.set_is_gameover(False)
            else:
                print("Did not click side (replay, save, load, restart) buttons")
        else:
            raise Exception("Incorrect board size. Something went wrong")
    
    '''
    This method handles removing a piece from the board, saves the current state to the backend log, and switches the turn
    '''
    def handle_remove_piece(self, clicked_pos):
        # if a piece can be removed
        if self.get_can_removepiece():
            # check if a mill was formed
            if self.get_board().form_mill(clicked_pos):
                # check if a moved or flown piece was from a previously formed mill
                self.get_board().check_remove_active_mill()
                # set check if a piece can be removed to false
                self.set_can_removepiece(False)
                # save current state to the log and switches the turn
                self.get_board().save_current_state_to_log()
                # check if the game is over or gridlocked (This gameover check only happens in 6 mens or 9 mens morris)
                if (self.get_board().is_game_over() or self.get_board().is_gridlocked()) and (self.get_board().get_board_size() == 6 or self.get_board().get_board_size() == 9) and self.get_board().get_remaining_turns() == 0:
                    self.set_is_gameover(True)
        # if no piece can be removed (aka no mill is formed), just save to log
        else:
            self.get_board().save_current_state_to_log()
            # DEBUG print("Can't remove a piece")

        
    def handle_main_game_click(self, clicked_pos):
        try:
            # Handle main game clicks based on the clicked position
            # DEBUG print(f"Main game click: {index}")
            # Add logic here

            # handle all the clicks with the side buttons (replay, save, load, restart)
            self.handle_side_btn_click(clicked_pos)
            # Placing pieces phase
            if self.get_board().get_remaining_turns() != 0:
                # player places a piece on the board
                if self.get_board().place_piece(clicked_pos):
                    # check if a moved or flown piece was from a previously formed mill
                    self.get_board().check_remove_active_mill()
                    # check if a mill was formed in the GUI, removepiece is set to true if 9 mens or 6 mens
                    if self.get_board().form_mill_GUI() and (self.get_board().get_board_size() == 6 or self.get_board().get_board_size() == 9):
                        self.set_can_removepiece(True)
                    # check if a mill was formed in the GUI, save state to log and it is gameover for 3 mens
                    elif self.get_board().form_mill_GUI() and self.get_board().get_board_size() == 3:
                        self.get_board().save_current_state_to_log()
                        self.set_is_gameover(True)
                    #else:
                        #print("Mill was not formed by this piece placement")
                    self.handle_remove_piece(clicked_pos)
            # Move/Fly piece phase
            elif self.get_board().get_remaining_turns() == 0:
                # check if the game is over or gridlocked, if so, game is over
                if self.get_board().is_game_over() or self.get_board().is_gridlocked():
                    self.set_is_gameover(True)

                # grab current position of player AND... 
                if self.get_startpos() == -1:
                    self.set_startpos(clicked_pos)
                    print(f"Start position: ", self.get_startpos())
                    print(f"End position (before click): ", self.get_endpos())
                    return
                # grab the end position of the player
                if self.get_endpos() == -1:
                    self.set_endpos(clicked_pos)
                    print(f"End position: ", self.get_endpos())
            
                # start of fly piece logic (you can only fly pieces in 9 mens or 6 mens)
                if self.get_board().player_piece_count() == 3 and (self.get_board().get_board_size() == 6 or self.get_board().get_board_size() == 9):
                    # player flies a piece
                    if self.get_board().fly_piece(self.get_startpos(), self.get_endpos()):
                        # check if a flown piece was from a previously formed mill
                        self.get_board().check_remove_active_mill()
                        # check if a mill was formed in the GUI
                        if self.get_board().form_mill_GUI():
                            # set the check if a piece can be removed to true
                            self.set_can_removepiece(True)
                    else:
                        # reset current position of piece flown and end position of piece flown
                        self.set_startpos(-1)
                        self.set_endpos(-1)
                        return
                # start of move piece logic
                else:
                    if self.get_board().move_piece(self.get_startpos(), self.get_endpos()):
                        # check if a moved piece was from a previously formed mill
                        self.get_board().check_remove_active_mill()
                        # check if a mill was formed in the GUI and if it is 6 mens or 9 mens
                        if self.get_board().form_mill_GUI() and (self.get_board().get_board_size() == 6 or self.get_board().get_board_size() == 9):
                            # set the check if a piece can be removed to true
                            self.set_can_removepiece(True)
                        # check if a mill was formed in the GUI and if it is 3 mens
                        elif self.get_board().form_mill_GUI() and self.get_board().get_board_size() == 3:
                            # save the current state to the log and switch turn
                            self.get_board().save_current_state_to_log()
                            # the game is over
                            self.set_is_gameover(True)
                    else:
                        # reset current position of piece moved and end position of piece moved
                        # This statement could be executed if the user makes a mistake of clicking on the wrong piece or wrong position
                        self.set_startpos(-1)
                        self.set_endpos(-1)
                        return
                # call method that removes piece, saves current state of game to the backend log, and switches turn
                self.handle_remove_piece(clicked_pos)
                # reset current position of piece flown and end position of piece flown
                self.set_startpos(-1)
                self.set_endpos(-1)
        except Exception as e:
            print(f"Error handling main game click: {e}")
    
    
    #This method is called when the game mode is human v computer and handles the computer placement, movement, and flying

    def handle_computer_turn(self):
        selections = [0, 0]
        # initialize computer remove piece position to 0
        remove_piece = 0
        # place piece phase
        if self.get_board().get_remaining_turns() != 0:
            # computer places piece
            self.get_board().computer_place_piece()
            # check to see if the placement formed a mill and if it is 6 mens or 9 mens morris, they can remove a piece
            if self.get_board().form_mill_GUI() and (self.get_board().get_board_size() == 6 or self.get_board().get_board_size() == 9):
                self.set_can_removepiece(True)
                remove_piece = self.get_board().computer_remove_piece()
            # check to see if the placement formed a mill and if it is 3 mens
            # if so the game is over
            elif self.get_board().form_mill_GUI() and self.get_board().get_board_size() == 3:
                self.set_is_gameover(True)
                return
        # move/fly piece phase
        elif(self.get_board().get_remaining_turns() == 0):
            # if the computer player has more than 3 pieces left on the board, they can only move pieces
            if self.get_board().player_piece_count() != 3:
                selections = self.get_board().computer_move_piece()
            # if the computer player has only 3 pieces left on the board (in 9 mens and 6 mens morris), then they can fly pieces
            elif self.get_board().player_piece_count() == 3 and (self.get_board().get_board_size() == 6 or self.get_board().get_board_size() == 9):
                self.get_board().computer_fly_piece()
            
            # check to see if the move/fly formed a mill and if it is 6 mens or 9 mens morris, then they can remove a piece  
            if self.get_board().form_mill_GUI() and (self.get_board().get_board_size() == 6 or self.get_board().get_board_size() == 9):
                self.set_can_removepiece(True)
                remove_piece = self.get_board().computer_remove_piece()
            # check to see if the move/fly formed a mill and if it is 3 mens morris, then the game is over
            elif self.get_board().form_mill_GUI() and self.get_board().get_board_size() == 3:
                self.set_is_gameover(True)
                return
 
        self.handle_remove_piece(remove_piece)
    
    def get_current_state_and_log(self):
        if not os.path.exists(TEMP_LOG_PATH):
            print("No saved game states to replay.")
            return
        with open(TEMP_LOG_PATH, "rb") as file:
            log = pickle.load(file)
        
        if not log:
            print("Log is empty. Nothing to replay.")
            return
        
         # Save current state
        current_state = {
            'board_size': self.get_board().get_board_size(),
            'positions': self.get_board().get_positions(),
            'player_turn': self.get_board().get_player_turn(),
            'active_mills': self.get_board().get_active_mills(),
            'remaining_turns': self.get_board().get_remaining_turns(),
            'permissible_moves': self.get_board().get_permissible_moves(),
        }
        current_state_and_log = [log, current_state]
        return current_state_and_log
    
    # method helps with rewinding a move and moving forward a move in replay mode
    def replay_handler(self, clicked_pos, log, current_state):
        # save replay state into temp variable
        index = self.get_replay_state()
        replay_state = 0
        if log is None or current_state is None:
            print("Error: Log or current state is None")
            return
        
        if clicked_pos == 0: # rewind a move button
            if index != 0:
                index -= 1
                replay_state = index
            else:
                index = 0
                replay_state = index
            # go through the log of moves and set the state (Temporary variable) to the replay_state
            state = log[index]
            # change the visual of the board
            self.change_replay_board_state(state)
            return replay_state   
        elif clicked_pos == 2:
            if index != (len(log) - 1):
                index += 1
                replay_state = index
            else:
                index = 0
                replay_state = index
            # go through the log of moves and set the state (Temporary variable) to the replay_state
            state = log[index]
            # change the visual of the board
            self.change_replay_board_state(state)
            return replay_state   
        elif clicked_pos == 3: # exit play button
            replay_state = 0
            self.change_replay_board_state(current_state)
            return replay_state
        else:
            return
            
            

    # handle all the clicks of the replay buttons
    def handle_replay_click(self, clicked_pos):
        if clicked_pos == 0 or clicked_pos == 2: # rewind/forward a move button
            self.set_replay_state(self.replay_handler(clicked_pos, self.get_current_log_GUI()[0], self.get_current_log_GUI()[1]))
        elif clicked_pos == 1: # play button (This will trigger handle_play_events() method)
            self.set_play_loop(0)
            self.set_is_in_play(True)
            self.set_play_length(len(self.get_current_log_GUI()[0]))
            self.set_counter(time.time())
        elif clicked_pos == 3: # exit replay
            # reset the state of the board to be the current state before exiting replay mode
            self.set_replay_state(self.replay_handler(clicked_pos, self.get_current_log_GUI()[0], self.get_current_log_GUI()[1]))
            self.set_is_in_replay(False)
        
        
    # handles the play mode of replay mode
    def handle_play_events(self, event):
        #print("One of the play buttons was clicked")

        try:
            # go through play state clickables
            for i, rect in enumerate(self.get_play_clickables()):
                if rect.collidepoint(event.pos):
                    self.handle_play_click(i)
                    break
        except Exception as e:
            print(f"Error handling play events: {e}")
    
    # method that changes the visual of the board in replay mode
    def change_replay_board_state(self, state):
        self.get_board().set_board_size(state['board_size'])
        self.get_board().set_positions(state['positions'])
        self.get_board().set_player_turn(state['player_turn'])
        self.get_board().set_active_mills(state['active_mills'])
        self.get_board().set_remaining_turns(state['remaining_turns'])
        
    
    # handles all of the play clickable event clicks
    def handle_play_click(self, clicked_pos):
    
        if clicked_pos == 0: # play button
            self.set_is_paused(False)
            self.set_counter(time.time())
        elif clicked_pos == 1: # pause button
            self.set_is_paused(True)
            pause_play_loop = self.get_play_loop()
        elif clicked_pos == 2: # exit play
            self.set_is_in_play(False)
        
        # handles the play loop for play during replay
        # play loop is 0
        # play length is length of temp log - 1
        if self.get_play_loop() == (self.get_play_length()-1):
            self.set_counter(time.time())
            self.set_is_in_sleep(True)
        
        state = self.get_current_log_GUI()[0][self.get_play_loop()]

        self.change_replay_board_state(state)
        
        # when game is in pause
        if self.get_is_paused() == True:
            self.set_play_loop(pause_play_loop)
        # when game is in play
        elif self.get_is_paused() == False:
            self.set_play_loop(round( time.time() - self.get_counter()))
            self.set_is_in_sleep(True)


        #print("Play loop: ", self.get_play_loop())
        #sys.exit()
        
        # change display according to play loop
        #print("Board Positions: ", self.get_board().get_positions())
        #print("Play loop: ", self.get_play_loop())
        #print("Current log[0][0]: ", self.get_current_log()[0][0])
        #sys.exit()
        #print("State: ", self.get_current_log()[0][self.get_play_loop()])
        

        #print("Current log: ", self.get_current_log())
        #print("State: ", state)

    
    # method that handles game mode selection events
    def handle_game_mode_selection_events(self, event):
        try:
            for i, rect in enumerate(self.get_selection_clickables()):
                if rect.collidepoint(event.pos):
                    self.handle_selection_click(i)
                    break
        except Exception as e:
            print(f"Error handling selection events: {e}")
    
    # handles the click on the selection clickables (single or multiplayer)
    def handle_selection_click(self, clicked_pos):
        if clicked_pos == 0: 
            self.get_board().set_game_mode(1) # single player (human v computer)
            self.set_is_in_game_mode_selection(False)
        elif clicked_pos == 1:  
            self.get_board().set_game_mode(0) # multi player (human v human)
            self.set_is_in_game_mode_selection(False)
    

    # main game loop
    def game_loop(self):
        # DEBUG print("Initializing game window")
        screen.fill(WHITE)
        clock = pygame.time.Clock()
        #print("Entering game loop....")

        self.set_is_running(True)
        # this loops runs on forever until user quits (exits window)
        while self.get_is_running():
            try:
                # Event handling
                # handles game mode selection mode (During Load Game from Start Menu)
                if self.get_is_in_game_mode_selection():
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            # DEBUG print("Quit event detected. Closing game window...")
                            self.set_is_running(False)
                            if os.path.exists(TEMP_LOG_PATH):
                                os.remove(TEMP_LOG_PATH)
                            break
                        elif event.type == pygame.MOUSEBUTTONUP:
                            self.handle_game_mode_selection_events(event)
                # if the game state is not in game mode selection mode
                elif not self.get_is_in_game_mode_selection():
                    # handles load game during gameplay
                    if self.get_is_load():
                        self.get_board().load()
                        self.setup_coords_for_clickables()
                        self.setup_coords_for_replay_play_selection_clickables()

                        if os.path.exists(LOAD_VAR_PATH):
                            os.remove(LOAD_VAR_PATH)

                        fileWriter = open(LOAD_VAR_PATH, "w")
                        fileWriter.write('False')
                        fileWriter.close()

                        self.set_is_load(False)
                        self.set_is_in_game_mode_selection(True)
                    # if the game state is not in play mode (this is occurs in replay mode)
                    elif not self.get_is_in_play():
                        # go through all events
                        for event in pygame.event.get():
                            # DEBUG print(f"Event: {event}")
                            if event.type == pygame.QUIT:
                                # DEBUG print("Quit event detected. Closing game window...")
                                self.set_is_running(False)
                                if os.path.exists(TEMP_LOG_PATH): 
                                    os.remove(TEMP_LOG_PATH)
                                break
                            # if mouse button up, handle all the mouse up button events
                            elif event.type == pygame.MOUSEBUTTONUP:
                                self.handle_mouse_up_events(event)
                    # if the game state is in play mode (this is occurs in replay mode)
                    elif self.get_is_in_play():
                        print("Game play mode is in here")
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                            # DEBUG print("Quit event detected. Closing game window...")
                                self.set_is_running(False)
                                if os.path.exists(TEMP_LOG_PATH):
                                    os.remove(TEMP_LOG_PATH)
                                break
                            elif event.type == pygame.MOUSEBUTTONUP:
                                print("Play event triggered")
                                self.handle_play_events(event)
                        
                    # handles computer turn
                    if self.get_board().get_player_turn() == 2 and self.get_board().get_game_mode() == 1:
                        print("Game is in computer turn mode")
                        self.handle_computer_turn()
                        
            
                screen.fill(WHITE)
                # set the board image
                self.set_boardImg()
                # draw the board
                self.draw_board()
                # if sleep (this is for during play mode after the whole sequence of moves is played)
                print("Play loop (Counter): ", self.get_play_loop())
                # Draw replay and other buttons based on the game state
                self.draw_buttons()
                # draw the prompts for the user
                self.draw_game_info()

                if self.get_is_in_sleep() == True:
                    time.sleep(1)
                    self.set_is_in_sleep(False)
            
                # update display
                pygame.display.flip()
                # set frame rate
                clock.tick(60)
            except Exception as e:
                print(f"Error in game loop: {e}")
                self.set_is_running(False)
                break
    
    def handle_load_from_start_menu(self):
        if os.path.exists(LOAD_VAR_PATH):
            os.remove(LOAD_VAR_PATH)

        fileWriter = open(LOAD_VAR_PATH, "w")
        fileWriter.write('False')
        fileWriter.close()
        
        board = Game()
        self.set_board(board)
        self.get_board().load()
        self.setup_coords_for_clickables()
        self.setup_coords_for_replay_play_selection_clickables()
        self.set_is_in_game_mode_selection(True)
        self.set_is_load(False)


    # setup load game for after the start menu
    def setupLoadGame(self):
        variable_load = ""

        with open(LOAD_VAR_PATH, 'r') as file:
            variable_load = file.read()

        # if file content contains True, then the game is in load mode
        if(variable_load == 'True'):
            self.set_is_load(True)
        elif(variable_load == 'False'):
            self.set_is_load(False)
        
def setupBoard():
    board = Game()
    # Set up the new board
    board_size = 0
    computer = 0
    # Extract board size from the system (from the previous screen)
    if len(sys.argv) > 1:
        board_size_comm = sys.argv[1]
        board_size = int(board_size_comm[0])
        computer = int(board_size_comm[1])
    # Set up the board
    board.set_board_size(board_size)
    board.set_initial_positions()
    board.set_player_turn(1)
    board.set_initial_remaining_turns()
    board.set_initial_permissible_moves()
    board.set_game_mode(computer)
    return board

def main():
     # GUI_State class instance
    gamestate = GUI_State()
    gamestate.setupLoadGame()
    if gamestate.get_is_load():
        gamestate.handle_load_from_start_menu()
        gamestate.game_loop()
    else:
        gamestate.set_board(setupBoard())
        gamestate.setup_coords_for_clickables()
        gamestate.setup_coords_for_replay_play_selection_clickables()
        # start game loop
        gamestate.game_loop()
# start whole execution of front end
main()






