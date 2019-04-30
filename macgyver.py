import pygame
from pygame.locals import *
from macclass import *

pygame.init()
test = Level()
test.generate()
windows = pygame.display.set_mode((screen_size, screen_size))
test.display(windows)
while game:
    pygame.display.flip()
