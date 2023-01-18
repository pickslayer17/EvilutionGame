import random

from model.direction import Direction


class RandomMover:
    def __init__(self, cell, max_ticks):
        self.cell = cell
        self.max_ticks = max_ticks
        self.ticks_moved = 0
        self.side_to_move = 0

    def do_move(self):
        if self.ticks_moved == 0:
            self.side_to_move = random.randint(0, 8)
            self.ticks_moved = random.randint(1, self.max_ticks)

        if self.side_to_move < 8:
            self.cell.turn(Direction.get_name_by_number(self.side_to_move))
            self.cell.move()

        self.ticks_moved -= 1