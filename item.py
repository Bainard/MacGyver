import pygame
import random
from pygame.locals import *
from constantes import *


class Items(object):
    """docstring for Items. renvoyer juste un tuple random pour l"instant"""

    def __init__(self, maze):
        super(Items, self).__init__()
        self.maze = maze
        self.tile_x_needle = 0
        self.x_needle = self.tile_x_needle * sprite_size
        self.tile_y_needle = 0
        self.y_needle = self.tile_y_needle * sprite_size
        self.tile_x_ether = 0
        self.x_ether = self.tile_x_ether * sprite_size
        self.tile_y_ether = 0
        self.y_ether = self.tile_y_ether * sprite_size
        self.tile_x_tube = 0
        self.x_tube = self.tile_x_tube * sprite_size
        self.tile_y_tube = 0
        self.y_tube = self.tile_y_tube * sprite_size

    def random_pos(self, ):
        while self.maze.structure[self.tile_y_needle][self.tile_x_needle] != "0":
            self.tile_x_needle = random.randint(0, 14)
            self.x_needle = self.tile_x_needle * sprite_size
            self.tile_y_needle = random.randint(0, 14)
            self.y_needle = self.tile_y_needle * sprite_size
        while self.maze.structure[self.tile_y_ether][self.tile_x_ether] != "0":
            self.tile_x_ether = random.randint(0, 14)
            self.x_ether = self.tile_x_ether * sprite_size
            self.tile_y_ether = random.randint(0, 14)
            self.y_ether = self.tile_y_ether * sprite_size
            print(self.x_ether)
        while self.maze.structure[self.tile_y_tube][self.tile_x_tube] != "0":
            self.tile_x_tube = random.randint(0, 14)
            self.x_tube = self.tile_x_tube * sprite_size
            self.tile_y_tube = random.randint(0, 14)
            self.y_tube = self.tile_y_tube * sprite_size
            print(self.x_tube)
