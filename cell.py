class Cell:
    def __init__(self, color, position_x, position_y, size_x, size_y, strength):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.size_x = size_x
        self.size_y = size_y
        self.nutrition_index = 0.8
        self.is_alive = True
        self.is_disappear = False

        self.age = 0
        self.energy = 255
        self.speed = 2
        self.strength = strength

    def eat_another_cell(self, cell):
        self.energy += int(cell.energy / self.nutrition_index)
        cell.disappear()

    def disappear(self):
        self.energy = 0
        self.is_alive = False
        self.is_disappear = True

    def become_stronger(self):
        self.strength += 30

    def kill(self):
        self.is_alive = False
        self.speed = 0
        self.energy = 0
