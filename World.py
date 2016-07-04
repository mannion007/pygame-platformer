import pygame
from Character import Hero
from Level import Level
from Weapon import Orb

class World:

    worldArray =[]

    def __init__(self):
        self.level = Level()
        self.hero = Hero()
        self.orb = Orb()
        self.worldArray = self.level.tiles
        
    def update(self):
        self.hero.update()
        self.level.update(self.hero)
        self.orb.update(self.hero)

    def render(self, screen):
        screen.blit(self.level.render(), [0,0])
        screen.blit(self.hero.render(), (self.hero.position[0], self.hero.position[1]))
        pygame.draw.circle(screen, [255,255,255], self.orb.orbitPos, self.orb.getRadius())