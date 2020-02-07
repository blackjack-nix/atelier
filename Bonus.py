import pygame

class Bonus:
	def __init__(self, startX, startY, bonusNumber, zoom):
		self.caseX = startX
		self.caseY = startY
		self.bonus = bonusNumber
		self.sprite = self.getSprite(pygame.image.load("images/bonus/bonus.png"), zoom)

	def getSprite(self, image, zoom):
		Tab = []
		for j in range(2):
			for i in range(3):
				imTemp = image.subsurface((i*16),(j*16),16,16)
				imTemp = pygame.transform.scale(imTemp,(int(zoom/1.5),int(zoom/1.5)))
				Tab.append(imTemp)
		return Tab

	def dessine(self, surface, zoom):
		surface.blit(self.sprite[self.bonus], ((self.caseX * zoom) + zoom//5,(self.caseY * zoom) + zoom//5))

	def effect(self, player):
		if(self.bonus == 0 and player.nbBombeMax > 1):
			player.nbBombeMax -= 1
		if(self.bonus == 1 and player.rayonBombe > 1):
			player.rayonBombe -= 1
		if(self.bonus == 2 and player.lives > 1):
			player.lives -=1
		if(self.bonus == 3):
			player.nbBombeMax += 1
		if(self.bonus == 4):
			player.rayonBombe += 1
		if(self.bonus == 5):
			player.lives +=1

