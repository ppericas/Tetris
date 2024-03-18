# matrix of 10 squares of 20 px by 20 of height (+ walls)
# ---------------------------------------------------------------------------------------------------------------------
# imports
import pygame, os, random

pygame.init()

# ---------------------------------------------------------------------------------------------------------------------
# constants
## window
WIDTH, HEIGHT = 250, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

## sizes
SQUARE_SIZE = 25

## others
FPS = 60

# ---------------------------------------------------------------------------------------------------------------------
# class & functions
def draw_matrix():
    for i in range (9):
        for j in range (19):
            pygame.draw.rect(WIN, WHITE, pygame.Rect(i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_window():
    draw_matrix()
    pygame.display.update()

# main loop
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == '__main__':
    main()       