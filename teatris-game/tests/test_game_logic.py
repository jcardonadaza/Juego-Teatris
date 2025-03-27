import unittest
from src.game.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.game_logic = GameLogic()

    def test_collision_detection(self):
        # Test collision detection logic
        self.assertTrue(self.game_logic.check_collision())

    def test_generate_new_piece(self):
        # Test if a new piece is generated correctly
        piece = self.game_logic.generate_new_piece()
        self.assertIsNotNone(piece)

    def test_update_game_state(self):
        # Test if the game state updates correctly
        initial_state = self.game_logic.get_state()
        self.game_logic.update_game_state()
        updated_state = self.game_logic.get_state()
        self.assertNotEqual(initial_state, updated_state)

if __name__ == '__main__':
    unittest.main()