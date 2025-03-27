class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def clear_line(self, line):
        del self.board[line]
        self.board.insert(0, [0 for _ in range(self.width)])

    def is_line_complete(self, line):
        return all(self.board[line])

    def add_tetromino(self, tetromino, position):
        for y, row in enumerate(tetromino.shape):
            for x, value in enumerate(row):
                if value:
                    self.board[position[1] + y][position[0] + x] = value

    def remove_tetromino(self, tetromino, position):
        for y, row in enumerate(tetromino.shape):
            for x, value in enumerate(row):
                if value:
                    self.board[position[1] + y][position[0] + x] = 0

    def get_empty_lines(self):
        return [i for i in range(self.height) if self.is_line_complete(i)]