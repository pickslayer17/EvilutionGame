from enum import Enum

class Direction(Enum):
    EAST = (1, 0), 0
    WEST = (-1, 0), 1
    NORTH = (0, -1), 2
    SOUTH = (0, 1), 3
    EAST_NORTH = (1, -1), 4
    EAST_SOUTH = (1, 1), 5
    WEST_NORTH = (-1, -1), 6
    WEST_SOUTH = (-1, 1), 7

    @staticmethod
    def get_name_by_number(number):
        if number == 0:
            return Direction.EAST
        elif number == 1:
            return Direction.WEST
        elif number == 2:
            return Direction.NORTH
        elif number == 3:
            return Direction.SOUTH
        elif number == 4:
            return Direction.EAST_NORTH
        elif number == 5:
            return Direction.EAST_SOUTH
        elif number == 6:
            return Direction.WEST_NORTH
        elif number == 7:
            return Direction.WEST_SOUTH
