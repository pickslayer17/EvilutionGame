class CellMover:
    def __init__(self, cell, speed):
        self.cell = cell
        self.speed = speed

    def move_east(self):
        self.cell.position_x += self.speed

    def move_west(self):
        self.cell.position_x -= self.speed

    def move_north(self):
        self.cell.position_y += self.speed

    def move_south(self):
        self.cell.position_y -= self.speed

    def move_east_north(self):
        self.move_east()
        self.move_north()

    def move_east_south(self):
        self.move_east()
        self.move_south()

    def move_west_north(self):
        self.move_west()
        self.move_north()

    def move_west_south(self):
        self.move_west()
        self.move_south()