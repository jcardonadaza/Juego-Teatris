class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.rotation_index = 0
        self.position = [0, 0]  # Starting position (x, y)

    def rotate(self):
        self.rotation_index = (self.rotation_index + 1) % len(self.shape)

    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy

    def get_current_shape(self):
        return self.shape[self.rotation_index]