import unittest
from src.game.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_state(self):
        self.assertEqual(self.board.get_state(), [[0]*10 for _ in range(20)])

    def test_add_line(self):
        self.board.add_line(0)
        self.assertEqual(self.board.get_state()[0], [1]*10)

    def test_remove_line(self):
        self.board.add_line(0)
        self.board.remove_line(0)
        self.assertEqual(self.board.get_state()[0], [0]*10)

    def test_clear_full_lines(self):
        for i in range(20):
            self.board.add_line(i)
        self.board.clear_full_lines()
        self.assertEqual(self.board.get_state(), [[0]*10 for _ in range(20)])

if __name__ == '__main__':
    unittest.main()