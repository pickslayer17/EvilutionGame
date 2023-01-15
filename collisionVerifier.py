class CollisionVerifier:
    def __init__(self):
        self.cells = []
        self.VERIFY_INDEX = 10

    def add_cell(self, cell):
        self.cells.append(cell)

    def verify(self):
        for i, cell in enumerate(self.cells):
            for j, cell2 in enumerate(self.cells[i+1:]):
                self._do_verify(cell, cell2)

    def _do_verify(self, c, c2):
        if (
                self.approx_compar(c.position_x, c2.position_x, self.VERIFY_INDEX) and
                self.approx_compar(c.position_y, c2.position_y, self.VERIFY_INDEX) and
                (c.is_alive and c2.is_alive)
        ):
            self._eat_verify(c, c2)

    def _eat_verify(self, c, c2):
        if c.strength > c2.strength:
            c.eat_another_cell(c2)
        elif c2.strength > c.strength:
            c2.eat_another_cell(c)
        elif c.strength == c2.strength:
            c.become_stronger
            c2.become_stronger


    def approx_compar(self, x, y, index):
        return abs(x-y) <= index