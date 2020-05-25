#def render(self):
#    glEnable(GL_POINT_SMOOTH)
#    glPointSize(3)
#    glBegin(GL_POINTS)
#    for p in range(len(self.particles)):
#        glColor4fv(self.particles[p].color)
#        glVertex3fv((self.particles[p].x, self.particles[p].y, self.particles[p].z))
#        self.particles[p].update()
#    glEnd()

from queue import Queue

q = Queue()

# Places at End
# Grabs from Front
q.put('a')
q.put('b')

print(q.get())
