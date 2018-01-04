import pygame
import pygame.locals
from sys import exit

SCREEN_SIZE = (600, 600)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            exit()

        print(event)

    pygame.display.update()
