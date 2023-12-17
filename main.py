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
    random_x = randrange(*RANGE)
    random_y = randrange(*RANGE)
    random_pos = (random_x, random_y)
    return random_pos

snake = pygame.rect.Rect((0,0), (TILE_SIZE-2, TILE_SIZE-2))
snake.center = get_random_pos()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
food = pygame.image.load("Apple_video_game.svg.png").convert_alpha()
food  = pygame.transform.scale(food, (30, 30))
food_rect = food.get_rect()
food_rect.center = get_random_pos()
time, time_step = 0, 90


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dir = (0, - TILE_SIZE)
            if event.key == pygame.K_DOWN:
                snake_dir = (0, TILE_SIZE)
            if event.key == pygame.K_RIGHT:
                snake_dir = (TILE_SIZE, 0)
            if event.key == pygame.K_LEFT:
                snake_dir = (-TILE_SIZE, 0)

    SCREEN.fill("black")

    if snake.top < 0 or snake.bottom > HEIGHT or snake.right < 0 or snake.left > WIDTH:
        snake.center, food_rect.center = get_random_pos(), get_random_pos()
        length = 1
        snake_dir = (0, 0)
        segments = [snake.copy()]

    if pygame.Rect.colliderect(snake, food_rect):
        food_rect.center = get_random_pos()
        length +=1

    SCREEN.blit(food, food_rect)

    for segment in segments:
        pygame.draw.rect(SCREEN, 'green', segment)

    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()