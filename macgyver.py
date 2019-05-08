import pygame
from pygame.locals import *
from level import Level
from character import Character
from item import Items
from constantes import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

windows = pygame.display.set_mode((screen_size, screen_size))


# loading img
carac = pygame.transform.scale(pygame.image.load(
    "img/MacGyver.png").convert_alpha(), (sprite_size, sprite_size))
boss = pygame.image.load("img/boss.png").convert_alpha()
needle = pygame.transform.scale(pygame.image.load(
    "img/aiguille.png").convert_alpha(), (sprite_size, sprite_size))
ether = pygame.transform.scale(pygame.image.load(
    "img/ether.png").convert_alpha(), (sprite_size, sprite_size))
tube = pygame.transform.scale(pygame.image.load(
    "img/tube.png").convert_alpha(), (sprite_size, sprite_size))

# loading sound
sound_step = pygame.mixer.Sound("sound/footstep.wav")
sound_item = pygame.mixer.Sound("sound/item.ogg")
sound_gameover = pygame.mixer.Sound("sound/gameover.wav")
sound_win = pygame.mixer.Sound("sound/win.wav")

while main_loop:
    maze = Level()
    maze.generate()
    maze.display(windows)
    mac = Character(maze)
    item = Items(maze)
    item.random_pos()
    boss_pos = boss_pos
    item_count = 0
    print(item.forbiden_tulpes)
    while game:

        pygame.time.Clock().tick(300)
        for event in pygame.event.get():
            if event.type == QUIT:
                main_loop, game = 0,0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mac.move("right")
                    sound_step.play()
                if event.key == K_LEFT:
                    mac.move("left")
                    sound_step.play()
                if event.key == K_UP:
                    mac.move("up")
                    sound_step.play()
                if event.key == K_DOWN:
                    mac.move("down")
                    sound_step.play()
        if (mac.x, mac.y) == (item.x_ether, item.y_ether):
            item.x_ether, item.y_ether = 0, 0*sprite_size
            item_count += 1
            sound_item.play()
        if (mac.x, mac.y) == (item.x_tube, item.y_tube):
            item.x_tube, item.y_tube = 0, 1*sprite_size
            item_count += 1
            sound_item.play()
        if (mac.x, mac.y) == (item.x_needle, item.y_needle):
            item.x_needle, item.y_needle = 0, 2*sprite_size
            item_count += 1
            sound_item.play()
        if (mac.x, mac.y) == boss_pos:
            if item_count < 3:
                sound_gameover.play()
                print("game over")
                game = 0
                over_loop = 1
            if item_count == 3:
                sound_win.play()
                print("gagne")
                game = 0
                over_loop = 1
        maze.display(windows)
        windows.blit(boss, (boss_pos))
        windows.blit(needle, (item.x_needle, item.y_needle))
        windows.blit(ether, (item.x_ether, item.y_ether))
        windows.blit(tube, (item.x_tube, item.y_tube))
        windows.blit(carac, (mac.x, mac.y))
        pygame.display.flip()
    while over_loop:
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('Retry? Y/N', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = windows.get_rect().centerx
        textrect.centery = windows.get_rect().centery
        windows.blit(text, textrect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                main_loop, over_loop = 0,0
            if event.type == KEYDOWN:
                if event.key == K_y:
                    over_loop, game = 0, 1
                if event.key == K_n:
                    over_loop, main_loop = 0,0
