import unittest
from src.game.tetromino import Tetromino

class TestTetromino(unittest.TestCase):

    def setUp(self):
        self.tetromino = Tetromino()

    def test_initial_shape(self):
        self.assertIsNotNone(self.tetromino.shape)

    def test_rotate(self):
        original_shape = self.tetromino.shape
        self.tetromino.rotate()
        self.assertNotEqual(original_shape, self.tetromino.shape)

    def test_move_left(self):
        original_position = self.tetromino.position
        self.tetromino.move_left()
        self.assertEqual(self.tetromino.position[0], original_position[0] - 1)

    def test_move_right(self):
        original_position = self.tetromino.position
        self.tetromino.move_right()
        self.assertEqual(self.tetromino.position[0], original_position[0] + 1)

    def test_move_down(self):
        original_position = self.tetromino.position
        self.tetromino.move_down()
        self.assertEqual(self.tetromino.position[1], original_position[1] + 1)

if __name__ == '__main__':
    unittest.main()