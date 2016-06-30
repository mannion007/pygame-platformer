import pygame
import math
phi = math.pi * 2

class Orb:

    orbitRadius = 35
    minOrbitRadius = 35
    maxOrbitRadius = 300
    orbitPos = [0,0]

    def getRadius(self):
        return self.orbitRadius / 7

    def calculatePosition(self, origin, radius, time, reverse):
        if(reverse):
            time = time * -1
        angle = phi * time 
        rsa = radius * math.sin(angle)
        rca = radius * math.cos(angle)
        return (int(origin[0] + rca), int(origin[1] + rsa))

    def update(self, hero):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            if(self.orbitRadius < self.maxOrbitRadius):
                self.orbitRadius += 2
        else:
            if(self.orbitRadius > self.minOrbitRadius):
                self.orbitRadius -= 3

        self.orbitPos = self.calculatePosition([hero.position[0] + hero.tileSize[0] / 2, hero.position[1] + hero.tileSize[1] / 2], self.orbitRadius, pygame.time.get_ticks() * 0.001, hero.spriteFlipped)