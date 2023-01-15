import random

import pygame
from cell import Cell
from cellMover import CellMover
from positionVerifier import PositionVerifier
from randomMover import RandomMover
from collisionVerifier import CollisionVerifier
from lifeLaw import LifeLaw
from cellFactory import CellFactory
from cellPainter import CellPainter

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
    cell_factory = CellFactory(cell_color, display_width, display_height)

    for x in range(200):
        cell = cell_factory.create_cell()
        cellMover = CellMover(cell)
        randomMover = RandomMover(cellMover, max_ticks_one_side)
        cells.append(cell)
        r_movers.append(randomMover)

    cellPainter = CellPainter(cells)
    lifeLaw = LifeLaw(cells)

    positionVerifier = PositionVerifier(display_width, display_height)
    for cell in cells:
        positionVerifier.add_cell(cell)
    collisionVerifier = CollisionVerifier()
    collisionVerifier.VERIFY_INDEX = 2
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


        lifeLaw.life()
        for randomMover in r_movers:
            randomMover.do_move()

        positionVerifier.verify()
        collisionVerifier.verify()
        cellPainter.paint()

        # Drawing
        display.fill((255, 255, 255))
        for cell in cells:
            pygame.draw.rect(display, cell.color, (cell.position_x,cell.position_y, cell.size_x, cell.size_y))


        # update part
        pygame.display.update()
        clock.tick(60)

run_game()