import unittest
from GameFunctions import Game_Functions
from Board import Board
from unittest.mock import patch
import threading

class TestGameFunctions(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game_Functions()

    def tearDown(self):
        pass

    @patch('builtins.input', side_effect=["1"])
    def test_correct_place_piece(self, mock_input):
        self.game.place_piece()
        self.assertTrue(self.board.getBoardPositions()[1] == 1)
    
    @patch('builtins.input', side_effect=["-1", "29", "3"])
    def test_invalid_pos_place_piece(self, mock_input):
        self.game.place_piece()
        self.assertTrue(self.board.getBoardPositions()[3] == 1)
    '''
        @patch('builtins.input', side_effects=["hello", "%$#", "quit"])
        def test_invalid_input_place_piece(self, mock_input):
        with self.assertRaises(ValueError) as context:
            finished_turn = self.game.place_piece()
            self.assertTrue(finished_turn)

        self.assertEqual(str(context.exception), "An error has occurred")
    
    
    @patch('builtins.input', side_effects=["1", "1", "0"])
    def test_occupied_place_piece(self, mock_input):
        finished_turn = self.game.place_piece()
        self.board.setPlrTurn(2 if self.board.getPlayerTurn() == 1 else 1)
        finished_turn = self.game.place_piece()
        self.assertTrue(finished_turn)
    '''





if __name__ == "__main__":
    unittest.main()



    



    
        
