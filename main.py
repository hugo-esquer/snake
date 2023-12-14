import pygame
from random import randrange

pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()
FPS = 60
TILE_SIZE = 30
RANGE = (TILE_SIZE // 2, WIDTH - TILE_SIZE // 2, TILE_SIZE // 2)
def get_random_pos():
    random_pos = ()
    random_x = randrange(*RANGE)
    random_y = randrange(*RANGE)
    random_pos = (random_x, random_y)
    return random_pos

snake = pygame.rect.Rect((0,0), (TILE_SIZE, TILE_SIZE))
snake.center = get_random_pos()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    SCREEN.fill("black")

    pygame.draw.rect(SCREEN, 'green', snake)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()