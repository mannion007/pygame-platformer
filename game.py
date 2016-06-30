import pygame
from random import randint
import numpy as np
from Character import Hero
from Level import Level
from Weapon import Orb

pygame.init()
 
########################
### Config Constants ###
########################
screenWidth = 480
screenHeight = 320
levelWidth = 4800
levelHeight = screenHeight
heroFrame = 0

##################
### Setup game ###
##################
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("My Lovely Game")
clock = pygame.time.Clock()

###############
## Variables ##
###############
done = False
level = Level(screen)
hero = Hero()
orb = Orb()

################# 
### Game loop ###
#################
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.startJump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.endJump()
 
    # Drawingddd
    screen.fill([255,0,0])
    
    # Update
    hero.update()
    level.update(hero)
    orb.update(hero)

    #Render
    level.render()    
    screen.blit(hero.render(), (hero.position[0], hero.position[1]))
    pygame.draw.circle(screen, [255,255,255], orb.orbitPos, orb.getRadius())

    # Update screen
    pygame.display.flip()

    # Framerate
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()