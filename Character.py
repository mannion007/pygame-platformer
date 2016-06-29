import pygame
import Spritesheet
import AnimatedSpritesheet

class Hero:
    
    tileSize = [30,48]
    speed = [0,0]
    
    frame = 0
    state = 'stand'
    position = [50,0]

    gravity = 0.75
    onGround = False


    def __init__(self):

        self.jog = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [16,15,14,13,12,11,10,9,8,7,6,5], pygame.Rect(0,0,30,48), True, 3)
        self.sprint = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [30,29,28,27,26,25,24,23,22,21], pygame.Rect(0,0,30,48), True, 2)
        self.stand = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [17,18,19,20], pygame.Rect(0,0,30,48), True, 9)
        self.jump = AnimatedSpritesheet.AnimatedSpritesheet('assets/hero.bmp', [4,3,2,1,0], pygame.Rect(0,0,30,48), True, 10)

        self.currentFrame = next(self.jump)

        self.updateHeroFrame()

    def updateHeroFrame(self):
        if(self.state == 'stand'):
            self.currentFrame = next(self.stand)
            self.jogFrames = 0
        elif(self.state == 'jog'):
            if(self.speed[0] < 4):
                if(self.speed[0] < 1.5):
                    self.speed[0] = 1.5
                else:
                    self.speed[0] += 0.025
            else :
                self.speed[0] = 4
            self.jogFrames += 1
            if(self.jogFrames < 125):
                self.currentFrame = next(self.jog)
            else:
                self.currentFrame = next(self.sprint)
        elif(self.state == 'jump'):
            self.currentFrame = next(self.jump)
        print(self.speed)


    def startJump(self):
        if(self.onGround):
            self.speed[1] = -16
            self.state = 'jump'
            self.onGround = False

    def endJump(self):
        if(self.speed[1] < -8):
            self.speed[1] = -8


    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_d]:
            if self.onGround:
                self.state = 'jog'
            else:
                self.speed[0] = 3
        elif keystate[pygame.K_a]:
            self.speed[0] = -1 * self.speed[0]
            if self.onGround:
                self.state = 'jog'
        elif(self.state != 'coast'):
            if self.onGround:
                self.state = 'stand'

        if(self.state == 'jog' and self.speed[0] < 3):
            self.speed[0] += 0.15
        elif(self.state == 'coast'):
            if(self.speed[0] >= 0):
                self.speed[0] -= 0.15
            else:
                self.speed[0] = 0
                self.state = 'stand'

        print(self.speed[0])

        self.speed[1] += self.gravity
        self.position[1] += self.speed[1]
        
        if(self.position[1] > 250):
            self.position[1] = 250
            self.speed[1] = 0
            self.onGround = True

        if(self.speed[0] > 0):
            if(self.position[0] < pygame.display.Info().current_w * 0.65 and self.speed[0] > 0):
                self.position[0] += self.speed[0]
        elif(self.speed[0] < 0):
            if(self.position[0] > 0):
                self.position[0] += self.speed[0]

    def render(self):
        if(self.state == 'stand'):
            self.currentFrame = next(self.stand)
        elif(self.state == 'jog'):
            self.currentFrame = next(self.jog)
        elif(self.state == 'jump'):
            self.currentFrame = next(self.jump)
        elif(self.state == 'coast'):
            self.currentFrame = next(self.stand)
        return self.currentFrame
        