from direction import Direction


class Cell:
    def __init__(self, color, position_x, position_y):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.direction = Direction.EAST
        self.size_x = 10
        self.size_y = 10
        self.nutrition_index = 0.8
        self.is_alive = True
        self.is_disappear = False

        self.age = 0
        self.energy = 100
        self.speed = 2
        self.strength = 50

