import pygame
from constantes import *


class Game(object):
    """docstring for game."""

    def __init__(self, item, windows, perso):
        super(Game, self).__init__()
        self.item = item
        self.gameover = 0
        self.win = 0
        self.game = 1
        self.over_loop = 0
        self.main_loop = 1
        self.windows = windows
        self.perso = perso
        self.sound_gameover = pygame.mixer.Sound("sound/gameover.wav")
        self.sound_win = pygame.mixer.Sound("sound/win.wav")
        self.message = ""

    def game_loop(self):
        if (self.perso.x, self.perso.y) == boss_pos:
            if self.item.item_count < 3:
                self.sound_gameover.play()
                print("game over")
                self.game = 0
                self.over_loop = 1
                self.message = "YOU LOSE! Try again? Y/N"
            if self.item.item_count == 3:
                self.sound_win.play()
                print("gagne")
                self.game = 0
                self.over_loop = 1
                self.message = "YOU WIN! Try again? Y/N"

    def end_loop(self):
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render(self.message, True, (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = self.windows.get_rect().centerx
        textrect.centery = self.windows.get_rect().centery
        self.windows.blit(text, textrect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    self.game, self.over_loop = 1, 0
                if event.key == pygame.K_n:
                    self.over_loop, self.game = 0, 0
