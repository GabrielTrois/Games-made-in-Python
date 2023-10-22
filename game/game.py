import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
screen.fill('dimgray')
pygame.display.set_caption('Dinosaur Game')
clock = pygame.time.Clock()

mountain = pygame.image.load('assets/images/mountain.png')
floor = pygame.image.load('assets/images/floor.png')
sky = pygame.image.load('assets/images/sky.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.blit(sky, (0, 0))
        screen.blit(floor, (0, 250))
        screen.blit(mountain, (0, 100))

    pygame.display.update()
    clock.tick(60)
