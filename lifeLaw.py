class LifeLaw:

    def __init__(self, cells):
        self.cells = cells

    def life(self):
        for cell in self.cells:
            if cell.is_disappear:
                self.cells.remove(cell)
            if not cell.is_alive:
                cell.kill()
            cell.age += 1
            cell.energy -= 1
            if cell.energy == 0:
                cell.kill()
