import pygame
import random
from sys import exit

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Flap.py')

background = pygame.image.load('images/background.png').convert()
background_rect = background.get_rect()

player_x = 200
player_y = 200
player_gravity = 0

while running := True:

    for event in pygame.event.get():    # event handler
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # jumping/flying
                if player_y > 0:    # will not decrease y if touching top
                    player_gravity -= 12.5

    if game_active := True:     # main gameplay loop
        screen.blit(background,background_rect)
 
        pygame.draw.circle(screen,(65,20,75),(player_x,player_y), 30)
        
        if player_y < 720:
            player_gravity += 0.5
            player_y += player_gravity  # falling

        if player_y < 0:
            player_y = 0   # sky limit
        elif player_y > 750:
            game_active = False     # exit main gameplay loop if player falls past y=750
    pygame.display.update()
    clock.tick(60)