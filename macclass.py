import pygame
from pygame.locals import *

class Level(object):
    """docstring for Level."""
    def __init__(self):
        super(Level, self).__init__()
        self.structure = []
        self.map = "maps/map.txt"
        self.wall = ""

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
            print(self.structure)

    def display(self):
