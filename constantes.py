import pygame
from pygame.locals import *

# Maze structure

floor_img = "img/floor.png"
wall_img = "img/wall.png"
number_of_sprite = 15
sprite_size = 40
screen_size = number_of_sprite * sprite_size

#Character
startx_mac = 5
starty_mac = 14
boss_pos = (7 * sprite_size, 0 * sprite_size)
item_count = 0

# maps file

map = "maps/map.txt"

# #load images
# pygame.init()
# carac = pygame.image.load("img/MacGyver.png").convert_alpha()
# boss = pygame.image.load("img/boss.png").convert_alpha()
# needle = pygame.transform.scale(pygame.image.load(
#     "img/aiguille.png").convert_alpha(), (sprite_size, sprite_size))
# ether = pygame.transform.scale(pygame.image.load(
#     "img/ether.png").convert_alpha(), (sprite_size, sprite_size))
# tube = pygame.transform.scale(pygame.image.load(
#     "img/tube.png").convert_alpha(), (sprite_size, sprite_size))

# loop

game = 1
