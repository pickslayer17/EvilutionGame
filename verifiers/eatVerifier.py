class EatVerifier:
    def __init__(self, cells):
        self.cells = cells

    def verify(self):
        for cell in self.cells:
            if cell.is_eaten:
                self.cells.remove(cell)