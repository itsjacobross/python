import random
import pygame
import numpy
import math

pygame.init()

class Dot:
    count=0

    def __init__(self, start=(0,0), end=(0,0), color=(0,0,255), size=10):
        self.curr  = start
        self.goal  = end
        self.color = color
        self.size  = size

    def move(self):
        sx = numpy.sign(self.goal[0]-self.curr[0])
        nx = self.curr[0] + sx
        sy = numpy.sign(self.goal[1]-self.curr[1])
        ny = self.curr[1] + sy
        self.curr = (nx,ny)

    def moveManhattan(self):
        if self.curr[0] != self.goal[0]:
            numpy_x   = numpy.sign(self.goal[0]-self.curr[0])
            new_x     = self.curr[0] + numpy_x
            self.curr = (new_x, self.curr[1])
        elif self.curr[1] != self.goal[1]:
            numpy_y   = numpy.sign(self.goal[1]-self.curr[1])
            new_y     = self.curr[1] + numpy_y
            self.curr = (self.curr[0], new_y)

    def moveLine(self):
        t = 0.1
        new_x = self.curr[0] + int((self.goal[0]-self.curr[0])*t)
        new_y = self.curr[1] + int((self.goal[1]-self.curr[1])*t)
        self.curr = (new_x,new_y)

pygame.init()
screen = pygame.display.set_mode([500, 500])
timer  = pygame.time.Clock()

ptA = (10,10)
ptB = (500,50)
d = Dot(ptA,ptB)

dots=[d]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for e in dots:
        pygame.draw.circle( screen, e.color, e.curr, e.size )
        e.moveLine()

    pygame.display.flip()
    timer.tick(30)

pygame.quit()
