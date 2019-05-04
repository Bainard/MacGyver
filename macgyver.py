import pygame
from pygame.locals import *
from level import Level
from character import Character
from item import Items
from constantes import *

pygame.init()
maze = Level()
maze.generate()
windows = pygame.display.set_mode((screen_size, screen_size))
maze.display(windows)
mac = Character(maze)
item = Items(maze)
item.random_pos()

#loading img
carac = pygame.transform.scale(pygame.image.load("img/MacGyver.png").convert_alpha(), (sprite_size, sprite_size))
boss = pygame.image.load("img/boss.png").convert_alpha()
needle = pygame.transform.scale(pygame.image.load(
    "img/aiguille.png").convert_alpha(), (sprite_size, sprite_size))
ether = pygame.transform.scale(pygame.image.load(
    "img/ether.png").convert_alpha(), (sprite_size, sprite_size))
tube = pygame.transform.scale(pygame.image.load(
    "img/tube.png").convert_alpha(), (sprite_size, sprite_size))
print((item.x_needle, item.y_needle))

while game:

    pygame.time.Clock().tick(300)
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

    # if mac are in the same pos than the boss
    # print((mac.x, mac.y))
    if (mac.x, mac.y) == (item.x_ether, item.y_ether):
        item.x_ether, item.y_ether = 0, 0
        item_count += 1
    if (mac.x, mac.y) == (item.x_tube, item.y_tube):
        item.x_tube, item.y_tube = 0, 0
        item_count += 1
    if (mac.x, mac.y) == (item.x_needle, item.y_needle):
        item.x_needle, item.y_needle = 0, 0
        item_count += 1
    if (mac.x, mac.y) == boss_pos:
        if item_count < 3:
            game = 0
            print("game over")
        if item_count == 3:
            game =0
            print("gagne")

    maze.display(windows)
    windows.blit(boss, boss_pos)
    windows.blit(needle, (item.x_needle, item.y_needle))
    windows.blit(ether, (item.x_ether, item.y_ether))
    windows.blit(tube, (item.x_tube, item.y_tube))
    windows.blit(carac, (mac.x, mac.y))
    pygame.display.flip()
