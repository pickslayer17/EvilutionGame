class CollisionVerifier:
    def __init__(self):
        self.cells = []
        self.VERIFY_INDEX = 10

    def add_cell(self, cell):
        self.cells.append(cell)

    def verify(self):
        for i, cell in enumerate(self.cells):
            for cell2 in self.cells[i + 1:]:
            #for j, cell2 in enumerate(self.cells[i+1:]):
                self._do_verify(cell, cell2)

    def _do_verify(self, c, c2):
        if (
                self.approx_compar(c.position_x, c2.position_x, self.VERIFY_INDEX) and
                self.approx_compar(c.position_y, c2.position_y, self.VERIFY_INDEX)
        ):
            pass


    def approx_compar(self, x, y, index):
        return abs(x-y) <= index