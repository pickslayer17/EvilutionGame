class Cell:
    def __init__(self, color, position_x, position_y, size_x, size_y):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.size_x = size_x
        self.size_y = size_y

        self.age = 0
        self.energy = 100
        self.speed = 4
