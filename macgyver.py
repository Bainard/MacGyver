import pygame
from pygame.locals import *
from level import Level
from character import Character
from item import Items
from constantes import *
from game import Game

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

windows = pygame.display.set_mode((screen_size, screen_size))

while main_loop:
    maze = Level()
    maze.generate()
    maze.display(windows)
    mac = Character(maze)
    item = Items(maze, mac)
    item.random_pos()
    game = Game(item, windows, mac)

    while game.game:
        pygame.time.Clock().tick(300)
        mac.move()
        item.pickup_item()
        game.game_loop()
        maze.display(windows)
        windows.blit(mac.boss, (boss_pos))
        windows.blit(item.needle, (item.x_needle, item.y_needle))
        windows.blit(item.ether, (item.x_ether, item.y_ether))
        windows.blit(item.tube, (item.x_tube, item.y_tube))
        windows.blit(mac.carac, (mac.x, mac.y))
        pygame.display.flip()
        if (game.game, game.over_loop) == (0, 0):
            main_loop = 0

    while game.over_loop:
        game.end_loop()
        print(game.game)
        if (game.game, game.over_loop) == (0, 0):
            main_loop = 0
