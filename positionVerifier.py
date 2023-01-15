class PositionVerifier:
    def __init__(self, cell, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
        self.cell = cell

    def verify(self):
        x = self.cell.position_x
        y = self.cell.position_y

        if x > self.display_width:
            self.cell.position_x = x - self.display_width

        if x < 0:
            self.cell.position_x = self.display_width + x

        if y > self.display_height:
            self.cell.position_y = y - self.display_height

        if y < 0:
            self.cell.position_y = self.display_height + y
