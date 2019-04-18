import pygame
from pygame.locals import *
from macclass import *

pygame.init()
test = Level()
test.generate()
windows = pygame.display.set_mode((300, 300))
test.display(windows)
pygame.display.flip()
