import pygame
from Character import Hero
from Level import Level
from Weapon import Orb

class World:

    tileSize = 16
    screenWidth = 480
    screenHeight = 320

    worldPosition = 0
    

    def __init__(self):
        self.level = Level()
        self.hero = Hero()
        self.orb = Orb()
        
    def update(self, keystate):
        self.hero.update(keystate)
        self.orb.update(self.hero)
        self.level.update(self.hero)



        if(not self.level.collisionCheck(self.hero.hitbox.move(int(self.hero.speed[0]), 0))):
            self.hero.hitbox = self.hero.hitbox.move(int(self.hero.speed[0]), 0)
        else:
            self.hero.speed[0] = 0

        if(not self.level.collisionCheck(self.hero.hitbox.move(0, int(self.hero.speed[1])))):
            self.hero.hitbox = self.hero.hitbox.move(0, int(self.hero.speed[1]))
        else:
            self.hero.onGround = True
            #self.hero.speed[1] = 0

    def render(self, screen):

        #startColumn = int(self.worldPosition / self.tileSize)
        #endColumn = int(startColumn + (self.screenWidth / self.tileSize) + self.level.tileBuffer)

        screen.blit(self.level.render(), [0,0])
        screen.blit(self.hero.render(), (self.hero.hitbox.left, self.hero.hitbox.top))
        pygame.draw.circle(screen, [255,255,255], self.orb.orbitPos, self.orb.getRadius())