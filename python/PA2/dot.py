import math
import pygame

# States/colors of the people.
unexposed = (0,0,255)
infected  = (255,165,0)
sick      = (255,0,0)
dead      = (0,0,0)
immune    = (0,255,0)

class Dot(pygame.sprite.Sprite):
    total_count     = 0
    unexposed_count = 0
    immune_count    = 0
    sick_count      = 0
    dead_count      = 0
    infected_count  = 0
    
    def __init__(self, start=(0,0), end=(0,0), state=unexposed,
                 size=6):
        self.home    = start
        self.curr    = self.home
        self.work    = end
        self.size    = size
        self.state   = state
        Dot.total_count     += 1
        Dot.unexposed_count += 1

        super().__init__()

        self.image = pygame.Surface([self.size,self.size], pygame.SRCALPHA)
        self.radius = self.size/2

        self.rect = self.image.get_rect()
        self.rect.x = self.home[0]
        self.rect.y = self.home[1]

    # Updates the location of the sprite/circle.
    def update(self):
        pygame.draw.circle(self.image, self.state, [int(self.size/2),int(self.size/2)], int(self.size/2))
        self.rect.x = self.curr[0]
        self.rect.y = self.curr[1]

    # Switches the start and stop positions.
    def reverse(self):
        temp = self.work
        self.work = self.home
        self.home = temp

    # Moves in a line.
    def moveLine(self):
        t = 0.01
        if (((self.curr[0] < self.work[0]+0.75) and (self.curr[0] > self.work[0]-0.75)) or ((self.curr[1] < self.work[1]+0.75) and (self.curr[1] > self.work[1]-0.75))):
            self.reverse()
        new_x = self.curr[0] + ((self.work[0]-self.home[0])*t)
        new_y = self.curr[1] + ((self.work[1]-self.home[1])*t)
        self.curr = (new_x,new_y)

    # Person becomes infected.
    def becomeInfected(self):
        self.state   = infected
        self.day     = 0
        Dot.infected_count  += 1
        Dot.unexposed_count -= 1

    # Person becomes sick.
    def becomeSick(self):
        self.state   = sick
        self.day     = 0
        Dot.sick_count     += 1
        Dot.infected_count -= 1

    # Person becomes dead.
    def becomeDead(self):
        self.state   = dead
        self.home    = self.curr
        self.work    = self.curr
        Dot.dead_count += 1
        Dot.sick_count -= 1

    # Person becomes immune.
    def becomeImmune(self):
        if self.state == sick:
            Dot.sick_count -= 1
        if self.state == infected:
            Dot.infected_count -= 1
        self.state   = immune
        Dot.immune_count += 1
