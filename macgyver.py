import pygame
from pygame.locals import *
from macclass import *

pygame.init()
maze = Level()
maze.generate()
windows = pygame.display.set_mode((screen_size, screen_size))
maze.display(windows)
mac = Character(maze)
carac = pygame.image.load("img/MacGyver.png").convert_alpha()
while game:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            game = 0
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mac.move("right")
            if event.key == K_LEFT:
                mac.move("left")
            if event.key == K_UP:
                mac.move("up")
            if event.key == K_DOWN:
                mac.move("down")


    # windows.blit(mac)
    maze.display(windows)
    windows.blit(carac, (mac.x, mac.y))
    pygame.display.flip()
