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


# loading img
carac = pygame.transform.scale(pygame.image.load(
    "img/MacGyver.png").convert_alpha(), (sprite_size, sprite_size))
boss = pygame.image.load("img/boss.png").convert_alpha()
needle = pygame.transform.scale(pygame.image.load(
    "img/aiguille.png").convert_alpha(), (sprite_size, sprite_size))
ether = pygame.transform.scale(pygame.image.load(
    "img/ether.png").convert_alpha(), (sprite_size, sprite_size))
tube = pygame.transform.scale(pygame.image.load(
    "img/tube.png").convert_alpha(), (sprite_size, sprite_size))




while main_loop:
    maze = Level()
    maze.generate()
    maze.display(windows)
    mac = Character(maze)
    item = Items(maze, mac)
    item.random_pos()
    game = Game(item,windows,mac)
    boss_pos = boss_pos


    while game.game:
        pygame.time.Clock().tick(300)
        mac.move()
        item.pickup_item()
        game.game_loop()
        maze.display(windows)
        windows.blit(boss, (boss_pos))
        windows.blit(needle, (item.x_needle, item.y_needle))
        windows.blit(ether, (item.x_ether, item.y_ether))
        windows.blit(tube, (item.x_tube, item.y_tube))
        windows.blit(carac, (mac.x, mac.y))
        pygame.display.flip()
        if (game.game, game.over_loop) == (0,0):
            main_loop = 0

    while game.over_loop:
        game.end_loop()
        print(game.game)
        if (game.game, game.over_loop) == (0,0):
            main_loop = 0
