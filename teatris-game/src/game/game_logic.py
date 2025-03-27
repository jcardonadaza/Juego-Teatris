def check_collision(board, tetromino, offset):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                board_x = x + tetromino.x + offset[0]
                board_y = y + tetromino.y + offset[1]
                if board_x < 0 or board_x >= len(board[0]) or board_y >= len(board):
                    return True
                if board_y >= 0 and board[board_y][board_x]:
                    return True
    return False

def merge_tetromino(board, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                board[tetromino.y + y][tetromino.x + x] = 1

def clear_lines(board):
    lines_to_clear = [i for i, row in enumerate(board) if all(row)]
    for i in lines_to_clear:
        del board[i]
        board.insert(0, [0 for _ in range(len(board[0]))])
    return len(lines_to_clear)

def generate_new_tetromino():
    import random
    shapes = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[0, 1, 0], [1, 1, 1]],  # T
        [[1, 1, 0], [0, 1, 1]],  # S
        [[0, 1, 1], [1, 1, 0]],  # Z
        [[1, 0, 0], [1, 1, 1]],  # L
        [[0, 0, 1], [1, 1, 1]],  # J
    ]
    shape = random.choice(shapes)
    return Tetromino(shape)  # Assuming Tetromino class has been defined in tetromino.py

def update_game_state(board, current_tetromino):
    if check_collision(board, current_tetromino, (0, 1)):
        merge_tetromino(board, current_tetromino)
        cleared_lines = clear_lines(board)
        current_tetromino = generate_new_tetromino()
        return board, current_tetromino, cleared_lines
    else:
        current_tetromino.y += 1
        return board, current_tetromino, 0