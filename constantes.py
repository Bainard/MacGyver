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
game = 1
