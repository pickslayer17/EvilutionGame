class CollisionVerifier:
    col_index = 1
    def __init__(self, cells):
        self.cells = cells
        self.VERIFY_INDEX = 45

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
            if c.strength > c2.strength:
                c.eat(c2)
            else:
                c2.eat(c)
            CollisionVerifier.col_index += 1
            pass


    def approx_compar(self, x, y, index):
        return abs(x-y) <= index