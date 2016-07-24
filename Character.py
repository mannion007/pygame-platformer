import pygame
import Spritesheet
import AnimatedSpritesheet

class Hero:
    
    maxSpeed = 4
    accelleration = [0,0]
    friction = 0.25
    gravity = 0.75
    spriteFlipped = False

    width = 30
    height = 46

    positionX = 10
    positionY = 10

    speedX = 0
    speedY = 0

    collisionBuffer = 0

    def __init__(self):

        self.rect = pygame.Rect(self.positionX,self.positionY,self.width - self.collisionBuffer,self.height- self.collisionBuffer)
        self.targetRect = self.rect.copy()
        self.renderbox = pygame.Rect(self.positionX,self.positionY,self.width,self.height)

        self.jog = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [16,15,14,13,12,11,10,9,8,7,6,5], self.renderbox, True, 3)
        self.sprint = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [30,29,28,27,26,25,24,23,22,21], self.renderbox, True, 2)
        self.stand = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [17,18,19,20], self.renderbox, True, 9)
        self.jump = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [4,3,2,1,0], self.renderbox, True, 10)
    
        self.onGround = False
        self.currentFrame = self.jump.next()

    def startJump(self):

        if(self.onGround):
            self.speedY = -16
            self.onGround = False

    def endJump(self):

        if(self.speedY < -8):
            self.speedY = -8

    def update(self, keystate):

        if keystate[pygame.K_d]:
            self.spriteFlipped = False
            self.accelleration[0] = 1
            if(self.speedX < self.maxSpeed):
                self.speedX += self.accelleration[0]
            else:
                self.speedX = self.maxSpeed
        elif keystate[pygame.K_a]:
            self.spriteFlipped = True
            self.accelleration[0] = -1
            if(self.speedX > self.maxSpeed):
                self.speedX -= self.accelleration[0]
            else:
                self.speedX = -1 * self.maxSpeed
        else:
            if(self.onGround):
                if(self.accelleration[0] != 0):
                    self.accelleration[0] += self.friction

                if(self.speedX > 0):
                    self.speedX -= self.friction
                elif(self.speedX < 0):
                    self.speedX += self.friction

        # Always apply gravity
        self.speedY += self.gravity

        self.targetRect.left = self.rect.left + self.speedX
        self.targetRect.top = self.rect.top + self.speedY

    def render(self):
        if(self.onGround):
            if(self.speedX == 0):
                self.currentFrame = next(self.stand)
            else:
                self.currentFrame = next(self.jog)    
        else:        
            self.currentFrame = next(self.jump)

        return pygame.transform.flip(self.currentFrame, self.spriteFlipped, False)
        
        