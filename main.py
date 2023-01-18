import pygame
from model.cell import Cell
from verifiers.positionVerifier import PositionVerifier
from randomMover import RandomMover

pygame.init()
display_width = 1000
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def run_game():
    game = True

    cell_color = (50, 205, 50)
    cell_x = 400
    cell_y = 400
    cell_size_x = 10
    cell_size_y = 10

    cell = Cell(cell_color, cell_x, cell_y)
    randomMover = RandomMover(cell, 15)
    pos_verifier = PositionVerifier(display_width, display_height)
    pos_verifier.add_cell(cell)

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

        randomMover.do_move()
        pos_verifier.verify()

        # Drawing
        display.fill((255, 255, 255))
        pygame.draw.rect(display, cell.color, (cell.position_x,cell.position_y, cell.size_x, cell.size_y))


        # update part
        pygame.display.update()
        clock.tick(60)

run_game()