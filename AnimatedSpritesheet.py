import pygame
import Spritesheet

class AnimatedSpritesheet(object):
    
    def __init__(self, filename, tileNumbers, mask, loop=True, delayFrames=1):
        self.loop = loop
        self.i = 0
        self.f = len(tileNumbers)
        sheet = Spritesheet.Spritesheet(filename, mask)
        
        self.delayFrames = delayFrames

        self.tiles = sheet.getTiles(tileNumbers)

    def iter(self):
        self.i = 0
        self.f = self.delayFrames
        return self

    def next(self):
        if self.i >= len(self.tiles):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.tiles[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.delayFrames
        return image