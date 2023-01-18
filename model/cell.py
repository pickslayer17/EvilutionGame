from model.direction import Direction
from model.randomMover import RandomMover


class Cell:
    def __init__(self, color = (50, 200, 50), position_x = 300, position_y = 300):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.direction = Direction.EAST
        self.size_x = 10
        self.size_y = 10
        self.nutrition_index = 0.8
        self.is_eaten = False
        self.is_alive = True

        self.age = 0
        self.energy = 100
        self.speed = 2
        self.strength = 50
        self.number = 0


    def turn(self, direction: Direction):
        self.direction = direction
    def move(self):
        self.position_x += self.direction.value[0][0] * self.speed
        self.position_y += self.direction.value[0][1] * self.speed
        pass

    def init_random_mover(self):
        self.rand_mover = RandomMover(self, 15)
    def move_random(self):
        self.rand_mover.do_move()

    def eat(self, cell):
        cell.is_eaten = True
        self.energy += cell.energy
