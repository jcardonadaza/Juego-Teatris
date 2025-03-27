def clear_lines(board):
    """Remove completed lines from the board and return the number of cleared lines."""
    cleared_lines = 0
    for i in range(len(board)):
        if all(board[i]):
            cleared_lines += 1
            board.pop(i)
            board.insert(0, [0 for _ in range(len(board[0]))])  # Add a new empty line at the top
    return cleared_lines

def rotate_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise."""
    return [list(reversed(col)) for col in zip(*matrix)]

def is_valid_position(board, shape, offset):
    """Check if the shape can be placed at the given offset on the board."""
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board_x = x + offset[0]
                board_y = y + offset[1]
                if board_x < 0 or board_x >= len(board[0]) or board_y >= len(board):
                    return False
                if board_y >= 0 and board[board_y][board_x]:
                    return False
    return True

def get_random_shape(shapes):
    """Return a random shape from the list of shapes."""
    import random
    return random.choice(shapes)