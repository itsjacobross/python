import random
import pygame
pygame.init()

class Dot:
    def __init__(self, position=(250,250), color=(0,0,255), size=75):
        self.position = position
        self.color = color
        self.size = size

screen = pygame.display.set_mode([500, 500])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    mydot = Dot()
    mydot.position = (random.randint(0,499),random.randint(0,499))
    mydot.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    mydot.size = random.randint(2,75)

    pygame.draw.circle(screen, mydot.color, mydot.position, mydot.size)

    pygame.display.flip()

pygame.quit()
5
