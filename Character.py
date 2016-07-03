import pygame
import Spritesheet
import AnimatedSpritesheet

class Hero:
    
    tileSize = [30,48]
    speed = [0,0]
    maxSpeed = 4
    accelleration = [0,0]
    friction = 0.25
    position = [50,0]
    gravity = 0.75
    spriteFlipped = False

    hasWorldCollission = False

    def __init__(self):
        self.jog = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [16,15,14,13,12,11,10,9,8,7,6,5], pygame.Rect(0,0,30,48), True, 3)
        self.sprint = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [30,29,28,27,26,25,24,23,22,21], pygame.Rect(0,0,30,48), True, 2)
        self.stand = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [17,18,19,20], pygame.Rect(0,0,30,48), True, 9)
        self.jump = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [4,3,2,1,0], pygame.Rect(0,0,30,48), True, 10)
        self.onGround = False
        self.currentFrame = self.jump.next()

    def startJump(self):
        if(self.onGround):
            self.speed[1] = -16
            self.onGround = False

    def endJump(self):
        if(self.speed[1] < -8):
            self.speed[1] = -8

    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_d]:
            self.spriteFlipped = False
            self.accelleration[0] = 1
            if(self.speed[0] < self.maxSpeed):
                self.speed[0] += self.accelleration[0]
            else:
                self.speed[0] = self.maxSpeed
        elif keystate[pygame.K_a]:
            self.spriteFlipped = True
            self.accelleration[0] = -1
            if(self.speed[0] > self.maxSpeed):
                self.speed[0] -= self.accelleration[0]
            else:
                self.speed[0] = -1 * self.maxSpeed
        else:
            if(self.onGround):
                if(self.accelleration[0] > 0):
                    self.accelleration[0] += self.friction
                elif(self.accelleration[0] < 0):
                    self.accelleration[0] += self.friction

                if(self.speed[0] > 0):
                    self.speed[0] -= self.friction
                elif(self.speed[0] < 0):
                    self.speed[0] += self.friction

        if(self.accelleration[0] > 0):
            if(self.position[0] < pygame.display.Info().current_w * 0.65):
                self.position[0] += int(self.speed[0])
        else:
            if(self.position[0] > 0):
                self.position[0] += int(self.speed[0])

        if(self.onGround == False):
            self.speed[1] += self.gravity
            self.position[1] += self.speed[1]
        
        # Collision check
        if(self.position[1] >= 242):
            self.position[1] = 242
            self.speed[1] = 0
            self.onGround = True

    def render(self):
        if(self.onGround):
            if(self.speed[0] == 0):
                self.currentFrame = next(self.stand)
            else:
                self.currentFrame = next(self.jog)    
        else:        
            self.currentFrame = next(self.jump)

        return pygame.transform.flip(self.currentFrame, self.spriteFlipped, False)
        
        