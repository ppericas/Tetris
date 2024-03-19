# matrix of 10 squares of 20 px by 20 of height (+ walls)
# ---------------------------------------------------------------------------------------------------------------------
# imports
import pygame
from icecream import ic
pygame.init()

# ---------------------------------------------------------------------------------------------------------------------
# constants
## window
WIDTH: int= 250
HEIGHT: int = 500
WIN: tuple[int] = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')

BLACK: tuple[int] = (0, 0, 0)
WHITE: tuple[int] = (255, 255, 255)
LIGHT_GREY: tuple[int] = (210, 210, 210)
DARK_GREY: tuple[int] = (80, 80, 80)

## sizes
SQUARE_SIZE: int = 23

## others
FPS: int = 60

# ---------------------------------------------------------------------------------------------------------------------
# class & functions
def output_to_file(text:str) -> None:
    with open('debug_log.txt', 'a') as f:
        f.write(f'{text}\n')


ic.configureOutput(prefix='Debug| ', outputFunction = output_to_file, includeContext=True)


def draw_matrix() -> None:
    WIN.fill(LIGHT_GREY)
    for i in range(10):
        for j in range(20):
            pygame.draw.rect(WIN, WHITE, pygame.Rect(i * SQUARE_SIZE + i * 2, j * SQUARE_SIZE + j * 2, SQUARE_SIZE, SQUARE_SIZE))


def draw_window() -> None:
    draw_matrix()
    pygame.display.update()


# main loop
def main() -> None:
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
