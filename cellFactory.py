import random

from model.cell import Cell
from model.randomMover import RandomMover


class CellFactory:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
    def create_cells(self, count):
        cells = []
        for i in range(count):
            x = random.randint(1, self.display_width)
            y = random.randint(1, self.display_height)
            strength = random.randint(30, 75)
            cell = Cell(position_x=x, position_y=y)
            cell.init_random_mover()
            cell.strength = strength
            cell.number = i
            cells.append(cell)
        return cells
