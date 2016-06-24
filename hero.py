class Hero:

	spriteSheetWidth = 510
	spriteSheetHeight = 48
	tileWidth = 30
	tileHeight = 48

	def getTile(tileNumber, tileWidth, tileHeight):
	    row = tileNumber / (spriteSheetWidth/tileWidth)
	    column = tileNumber % (spriteSheetWidth/tileWidth)
	    x = column * tileSize
	    y = row * tileSize
	    return [x,y,tileWidth,tileHeight]

	def drawHero(spriteSheet, screen):
		screen.blit(spriteSheet, (50, 50), getTile(1, tileWidth, tileHeight))
