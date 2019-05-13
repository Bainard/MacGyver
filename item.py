import pygame
import random
from pygame.locals import *
from constantes import *


class Items(object):
    """Shuffle the position of the items, take two arguments:
        - the maze where the items will be placed
        - the character who gonna picke up the items"""

    def __init__(self, maze, charac_pos):
        super(Items, self).__init__()
        self.maze = maze
        self.tile_x_needle = 0
        self.x_needle = 0
        self.tile_y_needle = 0
        self.y_needle = 0
        self.tile_x_ether = 0
        self.x_ether = 0
        self.tile_y_ether = 0
        self.y_ether = 0
        self.tile_x_tube = 0
        self.x_tube = 0
        self.tile_y_tube = 0
        self.y_tube = 0
        self.forbiden_tulpes = [boss_pos_sprite, (startx_mac, starty_mac), ]
        self.charac_pos = charac_pos
        self.sound_item = pygame.mixer.Sound("sound/item.ogg")
        self.item_count = 0
        self.needle = pygame.transform.scale(pygame.image.load(
            "img/aiguille.png").convert_alpha(), (sprite_size, sprite_size))
        self.ether = pygame.transform.scale(pygame.image.load(
            "img/ether.png").convert_alpha(), (sprite_size, sprite_size))
        self.tube = pygame.transform.scale(pygame.image.load(
            "img/tube.png").convert_alpha(), (sprite_size, sprite_size))

    def random_posV2(self,):
        x, y = 0, 0
        while self.maze.structure[y][x] != "0"\
                or (x, y) in self.forbiden_tulpes:
            x = random.randint(0, 14)
            y = random.randint(0, 14)
        self.forbiden_tulpes.append((x, y))
        return(x, y)

    def random_pos(self, ):
        self.tile_x_needle, self.tile_y_needle = self.random_posV2()
        self.x_needle = self.tile_x_needle * sprite_size
        self.y_needle = self.tile_y_needle * sprite_size
        self.tile_x_tube, self.tile_y_tube = self.random_posV2()
        self.x_tube = self.tile_x_tube * sprite_size
        self.y_tube = self.tile_y_tube * sprite_size
        self.tile_x_ether, self.tile_y_ether = self.random_posV2()
        self.x_ether = self.tile_x_ether * sprite_size
        self.y_ether = self.tile_y_ether * sprite_size

    def pickup_item(self, ):
        if (self.charac_pos.x, self.charac_pos.y) == (self.x_ether, self.y_ether):
            self.x_ether, self.y_ether = 0, 0 * sprite_size
            self.item_count += 1
            self.sound_item.play()
        if (self.charac_pos.x, self.charac_pos.y) == (self.x_tube, self.y_tube):
            self.x_tube, self.y_tube = 0, 1 * sprite_size
            self.item_count += 1
            self.sound_item.play()
        if (self.charac_pos.x, self.charac_pos.y) == (self.x_needle, self.y_needle):
            self.x_needle, self.y_needle = 0, 2 * sprite_size
            self.item_count += 1
            self.sound_item.play()
