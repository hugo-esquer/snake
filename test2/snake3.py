import pygame, random
from enum import Enum
from collections import namedtuple

pygame.init()

direction = Enum("direction", ["RIGHT", "LEFT", "UP", "DOWN"])

point = namedtuple("point", "x", "y")

BLOCK_SIZE = 20

WIDTH, HEIGHT = 640, 480

# init display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game !")
clock = pygame.time.Clock()

# init game state
direction = direction.RIGHT

head = point(WIDTH/2, HEIGHT/2)
snake = [head, 
         point(head.x-BLOCK_SIZE, head.y),
         point(head.x-(2*BLOCK_SIZE), head.y)]

score = 0
food = None

def place_food():
    pass

def play_step():
    pass


pygame.quit()