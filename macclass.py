import pygame
from pygame.locals import *

class Level(object):
    """docstring for Level."""
    def __init__(self):
        super(Level, self).__init__()
        self.structure = []
        self.map = "maps/map.txt"
        self.wall = "img/wall.png"
        self.floor = "img/floor.png"
        self.sprite_size = 20


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

    def display(self, windows):
        wall = pygame.image.load(self.wall).convert()
        floor = pygame.image.load(self.floor).convert()
        line_num = 0
        for line in self.structure:
            case_num = 0
            for sprite in line:
                y = line_num * self.sprite_size
                x = case_num * self.sprite_size
                if sprite == "X":
                    windows.blit(wall, (x, y))
                if sprite == "0":
                    windows.blit(floor, (x, y))
                case_num += 1
            line_num += 1
