import os
import pickle
import sys
import time

import pygame

from Board import Game_Functions as Game_Functions

DEBUG = False

# look if the load_game.txt file exists and if it doesn't exist, then create it and save variable_load == false in it
if not os.path.exists("load_game.txt"):
    variable_load = 'False'
    
    # save load == false in load_game.txt
    variable_load = open("load_game.txt", "w+")
    variable_load.write('False')

# open("load_game.txt", "w+")
# read data in load_game.txt if load_game.txt is empty, then create load == true
# if load_game.txt is not empty, then create load == false

# open load_game.txt and save the data in load variable
variable_load = open("load_game.txt", "r")
variable_load = variable_load.read()


# set up new board
# if variable_load == 'False':
board_size = 9
# board_size = 0
# extract board size from system (from previous screen)
if(len(sys.argv) > 1):
    board_computer_variable = sys.argv[1]
    print("board_computer_variable: ", board_computer_variable)
    print(type(board_computer_variable))
    board_computer_variable = str(board_computer_variable)
    # take the first digit of the board_computer_variable and set it to board_size
    # take the second digit of the board_computer_variable and set it to computer
    board_size = int(board_computer_variable[0])
    computer = int(board_computer_variable[1])
    # print("board_size: ", board_size)
else:
    computer = 0
    # print("board_size: ", board_size)
    # print("computer: ", computer)


# Global Variables
board = Game_Functions()
# set up board
# board.set_board_size(9)

board.set_board_size(board_size)
board.set_initial_positions()
board.set_player_turn(1)
board.set_initial_remaining_turns()
board.set_initial_permissible_moves()


pygame.font.init()  # you have to call this at the start, 
                    # if you want to use this module.
myfont = pygame.font.SysFont('Arial', 18)
# Initialize pygame
print(" calling pygame.init()")
pygame.init()
print("pygame initialized")
# Set the size of the screen
screen = pygame.display.set_mode((600, 750))

pygame.display.set_caption("Nine Men Morris")
print("game window initialized")
# nine mens morris board images (3 mens, 6 mens, 9 mens)
boardImg3 = pygame.image.load('assets/3mens.png')
boardImg6 = pygame.image.load('assets/6mens.png')
boardImg9 = pygame.image.load('assets/dragon9mens.png')

# expand size of 3 mens and 6 mens boards
boardImg3 = pygame.transform.scale(boardImg3, (500, 500))
boardImg6 = pygame.transform.scale(boardImg6, (500, 500))
boardImg9 = pygame.transform.scale(boardImg9, (500, 500))

# avatar images
leafImg = pygame.image.load('assets/player1_30x30.png')
fireImg = pygame.image.load('assets/player2_30x30.png')
highImg = pygame.image.load('assets/high.png')
roboImg = pygame.image.load('assets/robo1.png')
pantherimg = pygame.image.load('assets/panther.png')
pantherimg = pygame.transform.scale(pantherimg, (30, 30))
dragonimg = pygame.image.load('assets/dragon.png')
dragonimg = pygame.transform.scale(dragonimg, (30, 30))

# restart button
restart_button = pygame.image.load('assets/restart.png')
# replay buttons
play_button = pygame.image.load('assets/play_button.png')
pause_button = pygame.image.load('assets/pause_button.png')
rewind_button = pygame.image.load('assets/rewind_button.png')
fast_forward_button = pygame.image.load('assets/fast_forward_button.png')
back_button = pygame.image.load('assets/back_button.png')
replay_button = pygame.image.load('assets/replay_button.png')
save_button = pygame.image.load('assets/save_button.png')
load_button = pygame.image.load('assets/load_button.png')
# rduce size of of the replay button images
play_button = pygame.transform.scale(play_button, (30, 30))
pause_button = pygame.transform.scale(pause_button, (30, 30))
rewind_button = pygame.transform.scale(rewind_button, (30, 30))
fast_forward_button = pygame.transform.scale(fast_forward_button, (30, 30))
back_button = pygame.transform.scale(back_button, (30, 30))
replay_button = pygame.transform.scale(replay_button, (30, 30))
save_button = pygame.transform.scale(save_button, (30, 30))
load_button = pygame.transform.scale(load_button, (30, 30))
restart_button = pygame.transform.scale(restart_button, (30, 30))


# game mode selection buttons
single_player = pygame.image.load('assets/single_player.png')
multi_player = pygame.image.load('assets/multi_player.png')
single_player = pygame.transform.scale(single_player, (30, 30))
multi_player = pygame.transform.scale(multi_player, (30, 30))


# coordinates of each board position in Board and corresponding position in the nine mens morris board image
print("images loaded")
coords = {}
if(board.get_board_size() == 9):
    coords = {
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
    }
elif(board.get_board_size() == 6):
    coords = {
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
    }
elif(board.get_board_size() == 3):
    coords = {
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
    }

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
selection_clickables = [pygame.Rect(c[0], c[1], 30, 30) for c in selection_coords.values()]
play_clickables = [pygame.Rect(c[0], c[1], 30, 30) for c in play_coords.values()]
replay_clickables = [pygame.Rect(c[0], c[1], 30, 30) for c in replay_coords.values()]
clickables = [pygame.Rect(c[0], c[1], 30, 30) for c in coords.values()]
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Functions to draw the game state
def draw_board(screen, board_img, positions, coords, replay, play, game_mode_selection, startpos):
    try:
        # Draw the background board
        screen.blit(board_img.convert(), (0, 0))
        
        # Draw borders around the clickable areas if in debug mode
        if DEBUG:
            clickable_areas = clickables if not replay and not play else replay_clickables if replay and not play else play_clickables
            for rect in clickable_areas:
                pygame.draw.rect(screen, BLACK, rect, 1)
        
        # Draw the pieces on the board
        for pos, value in enumerate(positions):
            x, y = coords[pos]
            piece_img = pantherimg.convert_alpha() if value == 1 else dragonimg.convert_alpha() if value == 2 else None
            if piece_img:
                screen.blit(piece_img, (x, y))
        
        # Highlight the selected piece with a green rectangle
        if startpos is not None:
            x, y = coords[startpos]
            pygame.draw.rect(screen, GREEN, (x, y, 30, 30), 3)
        
        # Draw the restart game button
        restart_btn_coord = coords[12] if board.get_board_size() == 3 else coords[19] if board.get_board_size() == 6 else coords[27] if board.get_board_size() == 9 else None
        if not replay:
            screen.blit(restart_button.convert_alpha(), restart_btn_coord)
        
        # Draw the selection buttons
        if game_mode_selection:
            screen.blit(single_player.convert_alpha(), selection_coords[1])
            screen.blit(multi_player.convert_alpha(), selection_coords[2])
        
        # Draw replay buttons based on the game state
        if not replay and not play:
            replay_btn_coord = coords[9] if board.get_board_size() == 3 else coords[16] if board.get_board_size() == 6 else coords[24] if board.get_board_size() == 9 else None
            save_btn_coord = coords[10] if board.get_board_size() == 3 else coords[17] if board.get_board_size() == 6 else coords[25] if board.get_board_size() == 9 else None
            load_btn_coord = coords[11] if board.get_board_size() == 3 else coords[18] if board.get_board_size() == 6 else coords[26] if board.get_board_size() == 9 else None
            screen.blit(replay_button.convert_alpha(), replay_btn_coord)
            screen.blit(save_button.convert_alpha(), save_btn_coord)
            screen.blit(load_button.convert_alpha(), load_btn_coord)
        
        # Draw replay buttons if in replay mode
        if replay and not play:
            screen.blit(rewind_button.convert_alpha(), replay_coords[1])
            screen.blit(play_button.convert_alpha(), replay_coords[2])
            screen.blit(fast_forward_button.convert_alpha(), replay_coords[3])
            screen.blit(back_button.convert_alpha(), replay_coords[4])
        
        # Draw play buttons if in play mode
        if replay and play:
            screen.blit(play_button.convert_alpha(), play_coords[1])
            screen.blit(pause_button.convert_alpha(), play_coords[2])
            screen.blit(back_button.convert_alpha(), play_coords[3])
    except Exception as e:
        print(f"Error drawing the board: {e}")

def draw_game_info(screen, game_functions, gameover, removepos, replay, game_mode_selection):
    texts = []
    
    if gameover:
        if replay:
            texts.append("In Replay Mode")
        else:
            texts.append(f"Game Over! Player {2 if game_functions.get_player_turn() == 1 else 1} wins!")
            texts.append("Close window to change game settings or click Restart")
    elif not game_mode_selection:
        if game_functions.get_remaining_turns() != 0:
            if removepos:
                texts.append(f"Player {1 if game_functions.get_player_turn() == 1 else 2} formed a mill!")
                texts.append("Select an opponent's piece to remove from the board.")
            elif replay:
                texts.append("In Replay Mode")
            else:
                texts.append(f"It's Player {1 if game_functions.get_player_turn() == 1 else 2}'s turn!")
                texts.append(f"Remaining Turns: {game_functions.get_remaining_turns()}")
        elif game_functions.get_remaining_turns() == 0:
            if removepos:
                texts.append(f"Player {1 if game_functions.get_player_turn() == 1 else 2} formed a mill!")
                texts.append("Select an opponent's piece to remove from the board.")
            elif replay:
                texts.append("In Replay Mode")
            else:
                texts.append(f"It's Player {1 if game_functions.get_player_turn() == 1 else 2}'s turn!")
                texts.append("It's time to move pieces! Select a piece to move then select the position you want to move to.")
    elif game_mode_selection:
        texts.append("Select Game Mode")

    for i, text in enumerate(texts):
        textsurface = myfont.render(text, False, (0, 0, 0))
        screen.blit(textsurface, (10, 600 + i * 30))

def set_replay(idx):
    print("replay function called")
    if not os.path.exists(board.TEMP_LOG_PATH):
        print("No saved game states to replay.")
        return

    with open(board.TEMP_LOG_PATH, "rb") as file:
        log = pickle.load(file)

    if not log:
        print("Log is empty. Nothing to replay.")
        return

    # Save current state
    current_state = {
        'board_size': board.get_board_size(),
        'positions': board.get_positions(),
        'player_turn': board.get_player_turn(),
        'active_mills': board.get_active_mills(),
        'remaining_turns': board.get_remaining_turns(),
        'permissible_moves': board.get_permissible_moves(),
    }
    currentstuff = [log, current_state]
    return currentstuff

def replay_handler(replay_option, log, replay_state, current_state):
    print("replay_option: ", replay_option)
    print("replay_state: ", replay_state)
    print("current_state: ", current_state)
    index = replay_state
    if log is None or current_state is None:
        print("Error: Log or current state is None")
        return

    if replay_option == 0:  # rewind a move button
        index = max(0, index - 1)
        replay_state = index
    elif replay_option == 2:  # fast forward button
        index = min(len(log) - 1, index + 1)
        replay_state = index
    elif replay_option == 3:  # exit replay button
        replay_state = 0
        current_state = current_state

    state = log[index]
    board.set_positions(state['positions'])
    board.set_player_turn(state['player_turn'])
    board.set_active_mills(state['active_mills'])
    board.set_remaining_turns(state['remaining_turns'])
    return replay_state

def game_loop(variable_load, computer):

    print("Initializing game window...")
    screen.fill(WHITE)
    clock = pygame.time.Clock()

    #print("Entering main game loop...")

    running = True
    startpos = None
    endpos = None
    removepos = False
    gameover = False
    replay = False
    replay_state = 0
    play = False
    pause = False
    sleep = False
    boardImg = None
    game_mode_selection = False
    plr_turn = 1
    loop_check = False
    selections = [0,0]
    while running:
        try:
            # Event handling
            if game_mode_selection == False:
                if play == False:
                    for event in pygame.event.get():
                        print(f"Event: {event}")  # This will print out each event captured
                        if event.type == pygame.QUIT:
                            print("Quit event detected. Closing game window...")
                            running = False
                            break
                        if event.type == pygame.MOUSEBUTTONUP:
                            if replay == True:
                                for idx, rect in enumerate(replay_clickables):
                                    if rect.collidepoint(event.pos):
                                        if idx == 0: # rewind a move button
                                            replay_state = replay_handler(idx, currentstuff[0], replay_state, currentstuff[1])
                                            break
                                        if idx == 1: # play button
                                            play_loop = 0
                                            play = True
                                            play_length = len(currentstuff[0])
                                            counter = time.time()
                                            break
                                        if idx == 2: # fast forward
                                            replay_state = replay_handler(idx  , currentstuff[0], replay_state, currentstuff[1])
                                            break
                                        if idx == 3: # exit replay button
                                            #print("here exit replay")
                                            replay_handler(idx  , currentstuff[0],  replay_state, currentstuff[1])
                                            replay = False
                                            break
                            if replay == False:
                                for idx, rect in enumerate(clickables):
                                    # print("the clickables are: ", enumerate(clickables))
                                    # print("The idx is: ", idx)
                                    # print("The rect is: ", rect)
                                    # print("here1")
                                    # print("event.pos: ", event.pos)
                                    if rect.collidepoint(event.pos):
                                        if(board.get_board_size() == 9):
                                            if(idx == 24):
                                                currentstuff = set_replay(idx)
                                                replay = True
                                                break
                                            elif(idx == 25):
                                                board.save()
                                                break
                                            elif(idx == 26):
                                                board.load()
                                                break
                                            elif(idx == 27):
                                                board.new_restart_game()
                                                gameover = False
                                                break
                                        elif(board.get_board_size() == 6):
                                            if(idx == 16):
                                                currentstuff = set_replay(idx)
                                                replay = True
                                                break
                                            elif(idx == 17):
                                                board.save()
                                                break
                                            elif(idx == 18):
                                                board.load()
                                                break
                                            elif(idx == 19):
                                                board.new_restart_game()
                                                gameover = False
                                                break
                                        elif(board.get_board_size() == 3):
                                            if(idx == 9):
                                                currentstuff = set_replay(idx)
                                                replay = True
                                                break
                                            elif(idx == 10):
                                                board.save()
                                                break
                                            elif(idx == 11):
                                                board.load()
                                                break
                                            elif(idx == 12):
                                                board.new_restart_game()
                                                gameover = False
                                                break
                                        if removepos == True:
                                            if board.form_mill(idx):
                                                board.check_remove_active_mill()
                                                removepos = False
                                                board.save_current_state_to_log()
                                                if board.is_game_over() and board.get_remaining_turns() == 0 and (board.get_board_size() == 6 or board.get_board_size() == 9):
                                                    gameover = True
                                                break
                                            break
                                        if board.get_remaining_turns() != 0:
                                            #print("here2")
                                            #print(f"Clicked on position: {idx}")
                                            if board.place_piece(idx):
                                                board.check_remove_active_mill()
                                                #print("here passed place piece")
                                                if board.form_mill_GUI() and (board.get_board_size() == 6 or board.get_board_size() == 9):
                                                    removepos = True
                                                    break
                                                elif board.form_mill_GUI() and board.get_board_size() == 3:
                                                    #print("Game over!")
                                                    board.save_current_state_to_log()
                                                    #print(f"Player {2 if board.get_player_turn() == 1 else 1} wins!")
                                                    gameover = True
                                                    break
                                                board.save_current_state_to_log()
                                                #print("Form mill GUI = ", board.form_mill_GUI())
                                                #print("Board size: ", board.get_board_size())
                                                break
                                        if board.get_remaining_turns() == 0:
                                                if board.is_game_over():
                                                    #print("Game over!")
                                                    #print(f"Player {2 if board.get_player_turn() == 1 else 1} wins!")
                                                    gameover = True
                                                    break
                                                if startpos == None:
                                                    startpos = idx
                                                    #print("startpos: ", startpos)
                                                    #print("Starting position (piece selected to move): ", startpos)
                                                    break
                                                else:
                                                    if startpos == idx:
                                                        break
                                                    endpos = idx
                                                    #print("Ending position (position to move to): ", endpos)
                                                    #print("endpos: ", endpos)
                                                    if board.player_piece_count() == 3 and (board.get_board_size() == 6 or board.get_board_size() == 9):
                                                        if board.fly_piece(startpos, endpos):
                                                            board.check_remove_active_mill()
                                                            if board.form_mill_GUI():
                                                                removepos = True
                                                                startpos = None
                                                                endpos = None
                                                                break
                                                            board.save_current_state_to_log()
                                                            startpos = None
                                                            endpos = None
                                                            break
                                                        else:
                                                            startpos = None
                                                            endpos = None
                                                    else:
                                                        if board.move_piece(startpos, endpos):
                                                            print("Moved piece from ", startpos, "to ", endpos)
                                                            board.check_remove_active_mill()
                                                            if board.form_mill_GUI() and (board.get_board_size() == 6 or board.get_board_size() == 9):
                                                                removepos = True
                                                                startpos = None
                                                                endpos = None
                                                                break
                                                            elif board.form_mill_GUI() and board.get_board_size() == 3:
                                                                #print("Game over!")
                                                                board.save_current_state_to_log()
                                                                #print(f"Player {2 if board.get_player_turn() == 1 else 1} wins!")
                                                                gameover = True
                                                                break
                                                            board.save_current_state_to_log()
                                                            startpos = None
                                                            endpos = None
                                                            break
                                                        else:
                                                            startpos = None
                                                            endpos = None
                                break
                if play == True:
                    for event in pygame.event.get():
                        print(f"Event: {event}")  # This will print out each event captured
                        if event.type == pygame.QUIT:
                            print("Quit event detected. Closing game window...")
                            running = False
                            break
                            
                        print("event.type: ", event.type)
                        if event.type == pygame.MOUSEBUTTONUP:
                            for idx, rect in enumerate(play_clickables):
                                if rect.collidepoint(event.pos):
                                    if idx == 0:
                                        pause = False
                                        counter = time.time()
                                        break
                                    if idx == 1:
                                        pause = True
                                        pause_play_loop = play_loop
                                        break
                                    if idx == 2:
                                        play = False
                                        break
                    if play_loop == (play_length-1):
                        counter = time.time()
                        sleep = True
                    state = currentstuff[0][play_loop]
                    board.set_board_size(state['board_size'])
                    board.set_positions(state['positions'])
                    board.set_player_turn(state['player_turn'])
                    board.set_active_mills(state['active_mills'])
                    board.set_remaining_turns(state['remaining_turns'])
                    board.set_permissible_moves(state['permissible_moves'])
                    if pause == True:
                        play_loop = pause_play_loop
                    if pause == False:
                        play_loop = round( time.time() - counter )

                # if player == 2's turn, then call the computer's turn
                # if(board.get_player_turn() == 2 and board.get_remaining_turns() == 0):
                #     plr_turn = board.get_player_turn()
                # print("Player turn: ", plr_turn)
                if board.get_player_turn() == 2 and computer == 1:
                    if board.get_remaining_turns() != 0:
                        board.computer_place_piece()

                        if board.form_mill_GUI() and (board.get_board_size() == 6 or board.get_board_size() == 9):
                            removepos = True
                            remove_piece = board.computer_remove_piece()

                        if board.form_mill_GUI() and board.get_board_size() == 3:
                            print("Game over!")
                            print(f"Player {2 if board.get_player_turn() == 1 else 1} wins!")
                            gameover = True
                            break

                        if removepos == True:
                            print("yo we here at computer remove piece")
                            if board.form_mill(remove_piece):
                                removepos = False
                                board.check_remove_active_mill()
                                print("we gotz problemz")
                    print("we here now where's next")
                    if board.get_remaining_turns() == 0:
                        if board.player_piece_count() != 3:
                            loop_check = True
                            selections = board.computer_move_piece()
                            # # exit the program if selections is None
                            # if computer == 1 and selections != [17,16]:
                            #     print("still failing!")
                            #     gameover = True
                            #     break


                        if board.player_piece_count() == 3 and (board.get_board_size() == 6 or board.get_board_size() == 9):
                            board.computer_fly_piece() # gotta write the method for this

                        if board.form_mill_GUI() and (board.get_board_size() == 6 or board.get_board_size() == 9):
                            removepos = True
                            remove_piece = board.computer_remove_piece()
                            print("remove piece on: ", removepos)
                            print("and the remove piece is: ", remove_piece)

                        if board.form_mill_GUI() and board.get_board_size() == 3:
                            print("Game over!")
                            print(f"Player {2 if board.get_player_turn() == 1 else 1} wins!")
                            gameover = True
                            break

                        if removepos == True:
                            if board.form_mill(remove_piece):
                                removepos = False
                                board.check_remove_active_mill()
                                print("apples smell good")
                        print(f"Player Turn is: {2 if board.get_player_turn() == 2 else 1}")
                    board.save_current_state_to_log()
                

            if game_mode_selection == True:
                for event in pygame.event.get():
                    print(f"Event: {event}")  # This will print out each event captured
                    if event.type == pygame.QUIT:
                        print("Quit event detected. Closing game window...")
                        running = False
                        break
                    #print("event.type: ", event.type)
                    #print("pygame.MOUSEBUTTONUP: ", pygame.MOUSEBUTTONUP)
                    if event.type == pygame.MOUSEBUTTONUP:
                        for idx, rect in enumerate(selection_clickables):
                            if rect.collidepoint(event.pos):
                                if idx == 0:    
                                    computer = 1
                                    game_mode_selection = False
                                    break
                                if idx == 1:
                                    computer = 0
                                    game_mode_selection = False
                                    break


            #print("startpos: ", startpos)
            #print("endpos: ", endpos)
            print("removepos: ", removepos)
            print("gameover: ", gameover)
            #print("Print test: ", test)
            # print("replay: ", replay)
            # print("play: ", play)
            # print("board positions: ", board.get_positions())
            #print("board player turn (after computer turn): ", board.get_player_turn())
            #print("Loop check: ", loop_check)
            print("computer move from: ", selections[0])
            print("computer move to: ", selections[1])
            #print("board positions: ", board.get_positions())
            #     # Add more event handling logic here for other phases
            # print("remaining turns: ", board.get_remaining_turns())
            # Drawing the game state
            #print("Calling draw_board()...")

            #print("Computer: ", computer)

            if variable_load == 'True':
                board.load()
                
                # save load == false in load_game.txt
                variable_load = open("load_game.txt", "w+")
                variable_load.write('False')
                variable_load.close()

                variable_load = 'False'

                game_mode_selection = True



                print(f'This is: {variable_load}')

                # open("load_game.txt", "r")
                # variable_load = variable_load.read()
                # print(variable_load)
            
            screen.fill(WHITE)
            if(board.get_board_size() == 9):
                boardImg = boardImg9
            elif(board.get_board_size() == 6):
                boardImg = boardImg6
            elif(board.get_board_size() == 3):
                boardImg = boardImg3
            
            draw_board(screen, boardImg, board.get_positions(), coords, replay, play, game_mode_selection, startpos)
            if sleep == True:
                time.sleep(1)
                sleep = False
            
            #print("Calling draw_game_info()...")
            draw_game_info(screen, board, gameover, removepos, replay, game_mode_selection)

            # Updating the display
            #print("Updating display...")
            pygame.display.flip()

            # Frame rate
            clock.tick(60)
            
        except Exception as e:
            print(f"Error in game loop: {e}")
            running = False

    print("Exiting game...")

    pygame.quit()
    sys.exit()


game_loop(variable_load, computer)