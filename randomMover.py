import random

class RandomMover:
    def __init__(self, cell_mover, max_ticks):
        self.cell_mover = cell_mover
        self.max_ticks = max_ticks
        self.ticks_moved = 0
        self.side_to_move = 0

    def do_move(self):
        if self.ticks_moved == 0:
            self.side_to_move = random.randint(0, 8)
            self.ticks_moved = random.randint(1, self.max_ticks)

        if self.side_to_move == 0:
            self.cell_mover.move_east()
        elif self.side_to_move == 1:
            self.cell_mover.move_west()
        elif self.side_to_move == 2:
            self.cell_mover.move_north()
        elif self.side_to_move == 3:
            self.cell_mover.move_south()
        elif self.side_to_move == 4:
            self.cell_mover.move_east_north()
        elif self.side_to_move == 5:
            self.cell_mover.move_east_south()
        elif self.side_to_move == 6:
            self.cell_mover.move_west_north()
        elif self.side_to_move == 7:
            self.cell_mover.move_west_south()
        elif self.side_to_move == 8:
            pass

        self.ticks_moved -= 1