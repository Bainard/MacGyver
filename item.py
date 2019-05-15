import pygame
import random
from pygame.locals import *
from constantes import *


class Items():
    """Shuffle the position of the items, take two arguments:
        - the maze where the items will be placed
        - the character who gonna picke up the items"""

    def __init__(self, maze, charac_pos):
        super(Items, self).__init__()
        self.maze = maze
        self.pos_item = {'needle': (0, 0), 'ether': (0, 0), 'tube': (0, 0), }
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

    def shuffle_pos(self,):
        """take random coordonate, check if this is not a wall
            or a position already taken """
        x, y = 0, 0
        while self.maze.structure[int(y / 40)][int(x / 40)] != "0"\
                or (x, y) in self.forbiden_tulpes:
            x = random.randint(0, 14) * sprite_size
            y = random.randint(0, 14) * sprite_size
        self.forbiden_tulpes.append((x, y))
        return(x, y)

    def random_pos(self, ):
        """assign a position for each item"""
        self.pos_item['needle'] = self.shuffle_pos()
        self.pos_item['ether'] = self.shuffle_pos()
        self.pos_item['tube'] = self.shuffle_pos()

    def pickup_item(self, ):
        """for pickup the items"""
        if (self.charac_pos.x, self.charac_pos.y) == self.pos_item['ether']:
            self.pos_item['ether'] = (0, 0 * sprite_size)
            self.item_count += 1
            self.sound_item.play()
        if (self.charac_pos.x, self.charac_pos.y) == self.pos_item['tube']:
            self.pos_item['tube'] = (0, 1 * sprite_size)
            self.item_count += 1
            self.sound_item.play()
        if (self.charac_pos.x, self.charac_pos.y) == self.pos_item['needle']:
            self.pos_item['needle'] = (0, 2 * sprite_size)
            self.item_count += 1
            self.sound_item.play()
