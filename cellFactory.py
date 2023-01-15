from cell import Cell
import random

class CellFactory:
    def __init__(self, cell_color, display_width, display_height):
        self.cell_color = cell_color
        self.display_width = display_width
        self.display_height = display_height

    def create_cell(self):
        return Cell(
            self.cell_color,
            random.randint(0, self.display_width ),
            random.randint(0, self.display_height ),
            10, 10,
            50 + random.randint(-20, 20)
        )
