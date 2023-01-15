class CellPainter:
    def __init__(self, cells):
        self.cells = cells

    def paint(self):
        for cell in self.cells:
            if not cell.is_alive:
                cell.color = (0, 0, 0)
                continue

            g = 255 if cell.energy > 255 else cell.energy if cell.energy > 0 else 0
            b = 255 if cell.strength > 255 else cell.strength if cell.strength > 0 else 0
            cell.color = (50, g, b)