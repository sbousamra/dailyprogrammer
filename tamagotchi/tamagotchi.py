import time
import sys
import pygame
pygame.init()
# tamagotchihappy = pygame.image.load("tamagotchihappy.gif")
# tamagotchihappyrect = tamagotchihappy.get_rect()
# tamagotchinormal = pygame.image.load("tamagotchinormal.gif")
# tamagotchinormalrect = tamagotchinormal.get_rect()
# tamagotchiunhappy = pygame.image.load("tamagotchiunhappy.gif")
# tamagotchiunhappyrect = tamagotchiunhappy.get_rect()
# tamagotchipooptold = pygame.image.load("tamagotchipooptold.gif")
# tamagotchipooptoldrect = tamagotchipooptold.get_rect()
# tamagotchipoopself = pygame.image.load("tamagotchipoopself.gif")
# tamagotchipoopselfrect = tamagotchipoopself.get_rect()
# tamagotchihungry = pygame.image.load("tamagotchihungry.gif")
# tamagotchihungryrect = tamagotchihungry.get_rect()
# tamagotchistarving = pygame.image.load("tamagotchistarving.gif")
# tamagotchistarvingrect = tamagotchistarving.get_rect()
# tamagotchitired = pygame.image.load("tamagotchitired.gif")
# tamagotchitiredrect = tamagotchitired.get_rect()
# tamagotchifellasleep = pygame.image.load("tamagotchifellasleep.gif")
# tamagotchifellasleeprect = tamagotchifellasleep.get_rect()
# tamagotchidead = pygame.image.load("tamagotchidead.gif")
# tamagotchideadrect = tamagotchidead.get_rect()

class Tamagotchi:
	def __init__(self, name):
		self.name = name
		self.hunger = 25
		self.tiredness = 10
		self.poop = 0

	def getGraphics(self):
		if self.isHungry():
			return "tamagotchiunhappy.gif"

		elif self.isVeryHungry():
			return "tamagotchihungry.gif"

		elif self.isExtremelyHungry():
			return "tamagotchistarving.gif"

		elif self.isAlive():
			return "tamagotchinormal.gif"

	def isHungry(self):
		return(self.hunger in range(50,75))

	def isVeryHungry(self):
		return(self.hunger in range(75,90))

	def isExtremelyHungry(self):
		return(self.hunger in range(90,100))

	def isAlive(self):
		return	(self.hunger < 100) and (self.tiredness < 100) and (self.poop < 100)

	def hungerTick(self, amount):
		self.hunger = self.hunger + amount

	def tirednessTick(self, amount):
		self.tiredness = self.tiredness + amount

	def poopTick(self, amount):
		self.poop = self.poop + amount

	def tick(self):
		self.hungerTick(1)
		self.tirednessTick(1)
		self.poopTick(0)

class Buttons:
	def __init__(self, tamagotchi):
		self.tamagotchi = tamagotchi
		self.size = width, height = 640, 480
		self.black = (0,0,0)
		self.font = pygame.font.SysFont('Arial', 25)
		self.screen = pygame.display.set_mode(self.size)
		self.mousePosition = pygame.mouse.get_pos()

	def hungerButton(self):
		hungerRectangle = pygame.draw.rect(self.screen, (255,0,0), (0,440,213,40), 0)
		self.screen.blit(self.font.render("Hunger", True, (0,0,0)), (0,440))	
		for event in pygame.event.get():
			if event.type == pygame.mouse.get_pressed():
				currentMouse = self.mousePosition
				print(currentMouse)
				if hungerRectangle.collidepoint(currentMouse):
					print("hello worked")
					self.tamagotchi.hunger = self.tamagotchi.hunger - 25

	def tirednessButton(self):
		tirednessRectangle = pygame.draw.rect(self.screen, (0,0,255), (213,440,213,40), 0)
		self.screen.blit(self.font.render("Tiredness", True, (0,0,0)), (213,440))
		for event in pygame.event.get():
			if event.type == pygame.mouse.get_pressed():
				if tirednessRectangle.collidepoint(self.mousePosition):
					self.tamagotchi.tiredness = 0

	def poopButton(self):
		poopRectangle = pygame.draw.rect(self.screen, (139,69,19), (426,440,213,40), 0)
		self.screen.blit(self.font.render("Toilet", True, (0,0,0)), (426,440))
		for event in pygame.event.get():
			if event.type == pygame.mouse.get_pressed():
				if poopRectangle.collidepoint(self.mousePosition):
					self.tamagotchi.poop = 0

	def runButtons(self):
		self.hungerButton()
		self.tirednessButton()
		self.poopButton()

class Game:
	def __init__(self, tamagotchi, buttons):
		self.tamagotchi = tamagotchi
		self.buttons = buttons

	def run(self):
		while self.tamagotchi.isAlive():
			self.tamagotchi.tick()
			currentImage = pygame.transform.scale(pygame.image.load(self.tamagotchi.getGraphics()), self.buttons.size)
			currentImageRec = currentImage.get_rect()
			self.buttons.screen.fill(self.buttons.black)
			self.buttons.screen.blit(currentImage, currentImageRec)
			time.sleep(1)
			self.buttons.runButtons()
			pygame.display.update()
			print(self.tamagotchi.hunger)

			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

basspet = Tamagotchi("basspet")
buttons = Buttons(basspet)
game = Game(basspet, buttons)
game.run()