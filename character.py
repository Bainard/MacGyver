import pygame
import random
from pygame.locals import *
from constantes import *


class Character(object):
    """docstring for Character.
    take 2 arguments: the maze where the caracter move and the direction"""

    def __init__(self, maze, ):
        super(Character, self).__init__()
        # maze object for the acces of the matrice in class level
        self.maze = maze
        # coordonate in tiles
        self.tile_x = startx_mac
        self.tile_y = starty_mac
        # coordonate in pxl
        self.x = startx_mac * sprite_size
        self.y = starty_mac * sprite_size


    def move(self, direction):
        if direction == "right":
            if self.tile_x < number_of_sprite - 1:
                if self.maze.structure[self.tile_y][self.tile_x + 1] != "X":
                    self.tile_x += 1
                    self.x = self.tile_x * sprite_size

        if direction == "left":
            if self.tile_x > 0:
                if self.maze.structure[self.tile_y][self.tile_x - 1] != "X":
                    self.tile_x -= 1
                    self.x = self.tile_x * sprite_size

        if direction == "up":
            if self.tile_y > 0:
                if self.maze.structure[self.tile_y - 1][self.tile_x] != "X":
                    self.tile_y -= 1
                    self.y = self.tile_y * sprite_size

        if direction == "down":
            if self.tile_y < number_of_sprite - 1:
                if self.maze.structure[self.tile_y + 1][self.tile_x] != "X":
                    self.tile_y += 1
                    self.y = self.tile_y * sprite_size
