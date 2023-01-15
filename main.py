import random

import pygame
from cell import Cell
from cellMover import CellMover
from positionVerifier import PositionVerifier
from randomMover import RandomMover
from collisionVerifier import CollisionVerifier

pygame.init()
display_width = 1000
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def run_game():
    game = True

    cell_color = (50, 205, 50)
    cell_x = 40
    cell_y = 40
    cell_size_x = 10
    cell_size_y = 10
    max_ticks_one_side = 15
    cells = []
    r_movers = []

    for x in range(200):
        cell = Cell(cell_color, cell_x + random.randint(0,display_width), cell_y + random.randint(0,display_height), cell_size_x, cell_size_y)
        cellMover = CellMover(cell, cell.speed)
        randomMover = RandomMover(cellMover, max_ticks_one_side)
        cells.append(cell)
        r_movers.append(randomMover)

    positionVerifier = PositionVerifier(display_width, display_height)
    for cell in cells:
        positionVerifier.add_cell(cell)
    collisionVerifier = CollisionVerifier()
    for cell in cells:
        collisionVerifier.add_cell(cell)

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
        for randomMover in r_movers:
            randomMover.do_move()

        positionVerifier.verify()
        collisionVerifier.verify()

        # Drawing
        display.fill((255, 255, 255))
        for cell in cells:
            pygame.draw.rect(display, cell.color, (cell.position_x,cell.position_y, cell.size_x, cell.size_y))


        # update part
        pygame.display.update()
        clock.tick(60)

run_game()