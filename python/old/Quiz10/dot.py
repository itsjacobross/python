# Dot class
########################################################
#  This is where I define my Dot class. Used for ...   #
#  Author:  Alex Pang                                  #
#  References:  stackoverflow-- url here   #
# ....


import numpy
import pygame

class Dot(pygame.sprite.Sprite):
    ''' asdfasdfaf '''
    
    count = 0       # number of dots in population

    def __init__(self, start=(0,0), end=(0,0), color=(255,0,255)):
        ''' # constructor with initial position'''

        self.start = start  # P0
        self.gps   = self.start  # position along the line
        self.goal  = end    # P1
        self.color = color
        self.size  = 5
        
        super().__init__()

        self.image = pygame.Surface([5,5], pygame.SRCALPHA)
        self.image.fill(self.color)
        self.image.set_colorkey(self.color)

        #pygame.draw.circle(self.image, self.color, self.gps, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = self.start[0]
        self.rect.y = self.start[1]

    def update(self):
        self.rect.x = self.gps[0]
        self.rect.y = self.gps[1]

    def stop(self):
        self.goal = self.gps
        self.start = self.gps

    def move(self): # "diagonal" move 1 step closer to goal
        sx = numpy.sign(self.goal[0]-self.gps[0])  # returns -1,0,1
        nx = self.gps[0] + sx
        sy = numpy.sign(self.goal[1]-self.gps[1])
        ny = self.gps[1] + sy
        self.gps = (nx,ny)

    def moveManhattan( self ):
        # write code to move from start_pos to end_pos in hor/ver
        sx = numpy.sign(self.goal[0]-self.gps[0])  # returns -1,0,1
        if sx:
            self.gps = (self.gps[0] + sx, self.gps[1])
        else:
            sy = numpy.sign(self.goal[1]-self.gps[1])
            self.gps = (self.gps[0], self.gps[1] + sy) 

    def moveLine( self ):
        if self.gps != self.goal:
        # write code to move in straight line
            dx = self.goal[0]-self.start[0]
        #sx = numpy.sign(dx)  # returns -1,0,1
            nx = round(self.gps[0] + 0.1*dx)
        
            dy = self.goal[1]-self.start[1]
        #sy = numpy.sign(dy)
            ny = round(self.gps[1] + 0.1*dy)
            self.gps = (int(nx), int(ny))
