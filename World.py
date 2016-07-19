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

        #self.worldPosition = 10

        self.hero.update(keystate)
        self.orb.update(self.hero)
        self.level.update(self.hero)

        # Check for X collision
        if(self.hero.speedX != 0):
            #firstRow = int(self.hero.positionY / self.tileSize)
            #lastRow = int((self.hero.positionY + self.hero.height) / self.tileSize + 1)
            #heroColumn = int(self.hero.positionX / self.tileSize)
            firstRow = int(self.hero.rect.top / self.tileSize)
            lastRow = int((self.hero.rect.bottom) / self.tileSize + 1)
            heroColumn = int(self.hero.rect.left / self.tileSize)

            if(self.hero.speedX > 0):
                lastColumn = self.worldPosition + (self.screenWidth / self.tileSize)
            elif(self.hero.speedX < 0):
                lastColumn = self.worldPosition / self.tileSize
            
            closestCollisionColumn = lastColumn
            
            if(self.hero.speedX > 0):
                for row in range(firstRow, lastRow, 1):
                    for column in range(heroColumn, lastColumn, 1):
                        if(self.level.tiles[row, column] != 0):
                            if(column < closestCollisionColumn):
                                closestCollisionColumn = column
                                break

            elif(self.hero.speedX < 0):
                for row in range(firstRow, lastRow):
                    for column in range(heroColumn, lastColumn, -1):
                        if(self.level.tiles[row, column] != 0):
                            if(column > closestCollisionColumn):
                                closestCollisionColumn = column + 1
                                break

            if(self.hero.speedX > 0):
                if(self.hero.targetRect.right < closestCollisionColumn * self.tileSize):
                    self.hero.rect.left = self.hero.targetRect.left
            elif(self.hero.speedX < 0):
                if(self.hero.targetRect.left >= closestCollisionColumn * self.tileSize):
                    self.hero.rect.left = self.hero.targetRect.left

        firstColumn = int(self.hero.rect.left / self.tileSize)
        lastColumn = int((self.hero.rect.right) / self.tileSize + 1)
        heroRow = int(self.hero.rect.top / self.tileSize)

        #falling
        if(self.hero.speedY > 0):
            lastRow = 19
        else:
            lastRow = 0

        closestCollisionRow = lastRow

        # falling
        if(self.hero.speedY > 0):
            for column in range(firstColumn, lastColumn, 1):
                for row in range(heroRow, lastRow, 1):
                    if(self.level.tiles[row, column] != 0):
                        if(row < closestCollisionRow):
                            closestCollisionRow = row
                            break

        elif(self.hero.speedY < 0):
            for column in range(firstColumn, lastColumn):
                for row in range(heroRow, lastRow, -1):
                    if(self.level.tiles[row, column] != 0):
                        if(row > closestCollisionRow):
                            closestCollisionRow = row
                            break

        if(self.hero.speedY > 0):

            if(self.hero.targetRect.bottom < closestCollisionRow * self.tileSize):
                self.hero.rect.top = self.hero.targetRect.top

            else:
                self.hero.rect.top = closestCollisionRow * self.tileSize - self.hero.height - 1
                self.hero.speedY = 0
                self.hero.onGround = True

        elif(self.hero.speedY < 0):
            if(self.hero.targetRect.top >= (closestCollisionRow +1) * self.tileSize):
                self.hero.endJump
                self.hero.rect.top = self.hero.targetRect.top

    def render(self, screen):

        screen.blit(self.level.render(), [self.worldPosition, 0])
        screen.blit(self.hero.render(), (self.hero.rect.left, self.hero.rect.top))
        
        pygame.draw.circle(screen, [255,255,255], self.orb.orbitPos, self.orb.getRadius())
        
        pygame.draw.rect(screen, [255,0,0], self.hero.rect)
        pygame.draw.rect(screen, [0,255,0], self.hero.targetRect)