import random
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

class Particle:
    def __init__(self, x=0, y=0, z=0, length=5, color=(1, 0, 0, 1), lifetime=200):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.length = length
        self.exploded = False
        self.lifetime = 0
        self.maxlifetime = int(random.uniform(lifetime*0.9, lifetime*1.1))
        self.velocity = [random.uniform(-0.5, 0.5), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]
        self.q = []

    def update(self):
        dt = 0.05
        if self.y > 10:
            self.exploded = True
        if self.lifetime == self.maxlifetime or self.y < 0:
            self.color = (0,0,0,0)
        if self.exploded:
            self.x += self.velocity[0] * dt * self.length
            self.y += self.velocity[1] * dt * self.length - 0.5 * 9.8 * (dt*self.length)** 2
            self.z += self.velocity[2] * dt * self.length
            self.lifetime += 1
        else:
            self.y += 0.1

        if self.exploded == True:
            if(len(self.q) == self.length):
                self.q.pop(0)
            self.q.append((self.x,self.y,self.z))

class Firework(Particle):
    def __init__(self,x=0,z=0,n=60,color=(1,0,0,1),length=5):
        self.x = x
        self.z = z
        self.n  = n
        self.color = color
        self.length = length
        self.particles = []

        for i in range(n):
            y = 0
            color = self.color
            self.particles.append(Particle(x, y, z, length, color))

    def render(self):
        glEnable(GL_POINT_SMOOTH)
        glPointSize(3)
        glBegin(GL_POINTS)
        for p in range(len(self.particles)):
            if self.particles[p].exploded == True:
                for item in self.particles[p].q:
                    print(item)
                    glColor4fv(self.particles[p].color)
                    glVertex3fv(item)
            else:
                glColor4fv(self.particles[p].color)
                glVertex3fv((self.particles[p].x, self.particles[p].y, self.particles[p].z))
            self.particles[p].update()
        glEnd()
