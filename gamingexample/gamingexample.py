import sys, pygame
pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)

tamagotchihappy = pygame.image.load("tamagotchihappy.gif")
tamagotchinormal = pygame.image.load("tamagotchinormal.gif")
tamagotchiunhappy = pygame.image.load("tamagotchiunhappy.gif")
tamagotchipooptold = pygame.image.load("tamagotchipooptold.gif")
tamagotchipoopself = pygame.image.load("tamagotchipoopself.gif")
tamagotchihungry = pygame.image.load("tamagotchihungry.gif")
tamagotchistarving = pygame.image.load("tamagotchistarving.gif")
tamagotchitired = pygame.image.load("tamagotchitired.gif")
tamagotchifellasleep = pygame.image.load("tamagotchifellasleep.gif")
tamagotchidead = pygame.image.load("tamagotchidead.gif")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



    screen.fill(black)
    pygame.display.flip