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
