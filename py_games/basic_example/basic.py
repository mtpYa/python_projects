import pygame
# from pygame.locals import *
import pygame.locals
from sys import exit

background_img = 'sushiplate.jpg'
mouse_img = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Hello, World!')

background = pygame.image.load(background_img).convert()
fish = pygame.image.load(mouse_img).convert_alpha()
fish_width = fish.get_width()
fish_heigh = fish.get_height()
fish_pos = (fish_width / 2, fish_heigh / 2)

while True:
    screen.blit(background, (0, 0))
    screen.blit(fish, fish_pos)

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.locals.MOUSEMOTION and \
                event.buttons[0] == 1:
            x, y = pygame.mouse.get_pos()

            if fish_pos[0] < x < fish_pos[0] + fish_width and \
                    fish_pos[1] < y < fish_pos[1] + fish_heigh:
                fish_pos = (fish_pos[0] + event.rel[0],
                            fish_pos[1] + event.rel[1])
                screen.blit(background, (0, 0))

                screen.blit(fish, fish_pos)

    pygame.display.update()
