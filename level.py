import pygame
import random
from pygame.locals import *
from constantes import *


class Level():
    """Construction of the Maze from a txt file, take 1 arguments
        the windows where the maze gonna be displayed"""

    def __init__(self):
        super(Level, self).__init__()
        self.structure = []
        self.map = map

    def generate(self):
        """ build a double entry list from map.txt """
        with open(self.map, "r") as maps:
            level_structure = []
            for line in maps:
                level_line = []
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                level_structure.append(level_line)
            self.structure = level_structure

    def display(self, windows):
        """ display the sprites according to the double entry list"""
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
