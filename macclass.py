import pygame
import random
from pygame.locals import *
from constantes import *


class Level(object):
    """docstring for Level."""

    def __init__(self):
        super(Level, self).__init__()
        self.structure = []
        self.map = map

    def generate(self):
        with open(self.map, "r") as map:
            level_structure = []
            for line in map:
                level_line = []
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                level_structure.append(level_line)
            self.structure = level_structure

    def display(self, windows):
# load the image and transform the scale for the tile with a tuple of pixel
        wall = pygame.transform.scale(pygame.image.load(
            wall_img), (sprite_size, sprite_size))
        floor = pygame.transform.scale(pygame.image.load(
            floor_img), (sprite_size, sprite_size))
        line_num = 0
        for line in self.structure:
            case_num = 0
            for sprite in line:
                y = line_num * sprite_size
                x = case_num * sprite_size
                if sprite == "X":
                    windows.blit(wall, (x, y))
                if sprite == "0":
                    windows.blit(floor, (x, y))
                case_num += 1
            line_num += 1


class Character(object):
    """docstring for Character."""

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

class Items(object):
    """docstring for Items. renvoyer juste un tuple random pour l"instant"""
    def __init__(self, maze):
        super(Items, self).__init__()
        self.maze = maze
        self.tile_x_needle = 0
        self.x_needle = self.tile_x_needle *sprite_size
        self.tile_y_needle =0
        self.y_needle = self.tile_y_needle *sprite_size
        self.tile_x_ether = 0
        self.x_ether = self.tile_x_ether *sprite_size
        self.tile_y_ether =0
        self.y_ether = self.tile_y_ether *sprite_size
        self.tile_x_tube = 0
        self.x_tube = self.tile_x_tube * sprite_size
        self.tile_y_tube =0
        self.y_tube = self.tile_y_tube * sprite_size

    def random_pos(self, ):
        while self.maze.structure[self.tile_y_needle][self.tile_x_needle] != "0":
            self.tile_x_needle = random.randint(0,14)
            self.x_needle = self.tile_x_needle *sprite_size
            self.tile_y_needle = random.randint(0,14)
            self.y_needle = self.tile_y_needle *sprite_size
        while self.maze.structure[self.tile_y_ether][self.tile_x_ether] != "0":
            self.tile_x_ether = random.randint(0,14)
            self.x_ether = self.tile_x_ether *sprite_size
            self.tile_y_ether = random.randint(0,14)
            self.y_ether = self.tile_y_ether *sprite_size
        while self.maze.structure[self.tile_y_tube][self.tile_x_tube] != "0":
            self.tile_x_tube = random.randint(0,14)
            self.x_tube = self.tile_x_tube *sprite_size
            self.tile_y_tube = random.randint(0,14)
            self.y_tube = self.tile_y_tube *sprite_size
