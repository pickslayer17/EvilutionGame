import threading

import pygame

from cellFactory import CellFactory
from cellMonitor import CellMonitor
from model.cell import Cell
from verifiers.eatVerifier import EatVerifier
from verifiers.positionVerifier import PositionVerifier
from model.randomMover import RandomMover
from verifiers.collisionVerifier import CollisionVerifier

pygame.init()
display_width = 1000
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def run_game():
    game = True



    cellFactory = CellFactory(display_width, display_height)
    cells = cellFactory.create_cells(20)

    pos_verifier = PositionVerifier(cells, display_width, display_height)
    col_verifier = CollisionVerifier(cells)
    eat_verifier = EatVerifier(cells)
    cell_monitor = CellMonitor(cells)
    cell_monitor.print_cells_stats()

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

        for cell in cells:
            cell.move_random()
        pos_verifier.verify()
        col_verifier.verify()
        eat_verifier.verify()

        # Drawing
        display.fill((255, 255, 255))
        for cell in cells:
            pygame.draw.rect(display, cell.color, (cell.position_x,cell.position_y, cell.size_x, cell.size_y))

        # update part
        pygame.display.update()
        clock.tick(60)

run_game()