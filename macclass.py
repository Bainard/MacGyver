import pygame
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
            print(self.structure)

    def display(self, windows):
        # load the image and transform the scale for the tiles with a tuple of pixel size
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
        self.tile_x = 5
        self.tile_y = 14
        # coordonate in pxl
        self.x = 5 * 40
        self.y = 14 * 40
        #load the sprite of MacGyver

    def move(self, direction ):
        if direction == "right":
            if self.tile_x < number_of_sprite - 1:
                if self.maze.structure[self.tile_y][self.tile_x+1] != "X":
                    self.tile_x += 1
                    self.x = self.tile_x * sprite_size

        if direction == "left":
            if self.tile_x > 0:
                if self.maze.structure[self.tile_y][self.tile_x-1] != "X":
                    self.tile_x -= 1
                    self.x = self.tile_x * sprite_size

        if direction == "up":
            if self.tile_y >0:
                if self.maze.structure[self.tile_y-1][self.tile_x] != "X":
                    self.tile_y -= 1
                    self.y = self.tile_y * sprite_size

        if direction == "down":
            if self.tile_y < number_of_sprite - 1:
                if self.maze.structure[self.tile_y+1][self.tile_x] != "X":
                    self.tile_y += 1
                    self.y = self.tile_y * sprite_size
