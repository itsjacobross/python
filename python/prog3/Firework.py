import random
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class Particle:
    def __init__(self, x=0, y=0, z=0, length=0, color=(0, 0, 0, 1)):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.length = length
        self.exploded = False
        self.velocity = [random.uniform(-1, 1), random.uniform(5, 10), random.uniform(-1, 1)]

        self.trajectory = [(self.x,self.y,self.z)]
        dt = 0.05
        for i in range(1, self.length):
            x = self.x + self.velocity[0] * dt * i
            y = self.y + self.velocity[1] * dt * i - 0.5 * 9.8 * (dt*i)** 2
            z = self.z + self.velocity[2] * dt * i
            if y<0:
                y=0
            self.trajectory.append((x,y,z))

    def update(self):
        if self.y > 10:
            self.exploded = True
        if self.exploded:
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.z += self.velocity[2]
        else:
            self.y += 0.1

class Firework(Particle):
    def __init__(self,x=0,z=0,n=100,color=(0,0,0,1),length=0,stddev=0.1):
        self.x = x
        self.z = z
        self.n  = n
        self.color = color
        self.length = length
        self.stddev = stddev
        self.particles = []

        for i in range(n):
            color = self.color
            d1 = round(random.gauss(length, stddev)
            self.particles.append(Particle(x, y, z, d1, color))

    def render(self):
        glEnable(GL_POINT_SMOOTH)
        glPointSize(3)
        glBegin(GL_POINTS)
        for p in range(len(self.particles)):
            glColor4fv(self.particles[p].color)
            glVertex3fv((self.particles[p].x, self.particles[p].y, self.particles[p].z))
            self.particles[p].update()
        glEnd()
