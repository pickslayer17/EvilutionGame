class PositionVerifier:
    def __init__(self, cells, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
        self.cells = cells

    def verify(self):
        for cell in self.cells:
            x = cell.position_x
            y = cell.position_y

            if x > self.display_width:
                cell.position_x = x - self.display_width

            if x < 0:
                cell.position_x = self.display_width + x

            if y > self.display_height:
                cell.position_y = y - self.display_height

            if y < 0:
                cell.position_y = self.display_height + y
