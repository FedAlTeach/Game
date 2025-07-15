import sys

import pygame
from random import randint, randrange


pygame.init()
window = pygame.display.set_mode((400, 500))
rectangle = pygame.Rect(60, 80, 150, 200)
# color = (255, 155, 200)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mysurf = pygame.Surface((100, 100))
    mysurf.fill((5, 205, 255))
    mysurf.set_alpha(10)
    window.blit(mysurf, (100, 180))
    pygame.display.update()