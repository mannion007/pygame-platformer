import pygame

class Hero:

	spriteSheet = pygame.image.load("assets/hero.png")
	spriteSheetWidth = 630
	spriteSheetHeight = 48
	tileWidth = 30
	tileHeight = 48
	frame = 0
	state = 'stand'
	position = 50
	speed = 0

	def __init__(self, screen):
		self.screenWidth, self.screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
		self.screen = screen

	def getTile(self, tileNumber, tileWidth, tileHeight):
	    row = tileNumber / (self.spriteSheetWidth/self.tileWidth)
	    column = tileNumber % (self.spriteSheetWidth/self.tileWidth)
	    x = column * self.tileWidth
	    y = row * self.tileHeight
	    return [x, y, self.tileWidth, self.tileHeight]

	def move(self, speed):
		self.speed = speed
		
		if(self.speed == 0):
			self.state = 'stand'
			self.frame = 20
		elif(self.speed > 0):
			self.state = 'run'
			self.frame = 8
		elif(self.speed < 0):
			self.state = 'run'
			self.frame = 8

		if(self.speed > 0):
			if(self.position < self.screenWidth * 0.65 and self.speed > 0):
				self.position += self.speed
		elif(self.speed < 0):
			if(self.position > 0):
				self.position += self.speed
	def render(self):
	
		self.screen.blit(self.spriteSheet, (self.position, 250), self.getTile(self.frame, self.tileWidth, self.tileHeight))