import pygame
from cell import Cell
from cellMover import CellMover
from positionVerifier import PositionVerifier
from randomMover import RandomMover

pygame.init()
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def run_game():
    game = True

    cell = Cell((50, 205, 50), 40, 30, 10, 10)
    cellMover = CellMover(cell, 4)
    randomMover = RandomMover(cellMover, 15)
    positionVerifier = PositionVerifier(cell, display_width, display_height)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # keys
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     x += 2

        # LOGIC
        #cellMover.move_east()
        randomMover.do_move()
        positionVerifier.verify()

        # Drawing
        display.fill((255, 255, 255))
        pygame.draw.rect(display, cell.color, (cell.position_x,cell.position_y, cell.size_x, cell.size_y))

        # update part
        pygame.display.update()
        clock.tick(60)

run_game()