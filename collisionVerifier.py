class CollisionVerifier:
    def __init__(self):
        self.cells = []
        self.VERIFY_INDEX = 5
        self.color_1 = (250,128,114)
        self.color_2 = (176,224,230)

    def add_cell(self, cell):
        self.cells.append(cell)

    def verify(self):
        for i, cell in enumerate(self.cells):
            for j, cell2 in enumerate(self.cells[i+1:]):
                self._do_verify(cell, cell2)

    def _do_verify(self, c, c2):
        if self.approx_compar(c.position_x, c2.position_x, self.VERIFY_INDEX) and self.approx_compar(c.position_y, c2.position_y, self.VERIFY_INDEX):
            c.color = self.color_1
            c2.color = self.color_1

    def approx_compar(self, x, y, index):
        return abs(x-y) <= index