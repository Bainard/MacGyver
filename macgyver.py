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
sound_item = pygame.mixer.Sound("sound/item.ogg")
sound_gameover = pygame.mixer.Sound("sound/gameover.wav")
sound_win = pygame.mixer.Sound("sound/win.wav")

while main_loop:
    maze = Level()
    maze.generate()
    maze.display(windows)
    mac = Character(maze)
    item = Items(maze, mac)
    item.random_pos()
    boss_pos = boss_pos
    print(item.forbiden_tulpes)
    while game:
        pygame.time.Clock().tick(300)
        mac.move()
        item.pickup_item()
        if (mac.x, mac.y) == boss_pos:
            if item.item_count < 3:
                sound_gameover.play()
                print("game over")
                game = 0
                over_loop = 1
                message="YOU LOSE! Try again? Y/N"
            if item.item_count == 3:
                sound_win.play()
                print("gagne")
                game = 0
                over_loop = 1
                message="YOU WIN! Try again? Y/N"

        maze.display(windows)
        windows.blit(boss, (boss_pos))
        windows.blit(needle, (item.x_needle, item.y_needle))
        windows.blit(ether, (item.x_ether, item.y_ether))
        windows.blit(tube, (item.x_tube, item.y_tube))
        windows.blit(carac, (mac.x, mac.y))
        pygame.display.flip()

    while over_loop:
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render(message, True, (255, 0, 0))
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
