import random
import pygame
import numpy
import math
import dot
import itertools

dots=[]
sprites = pygame.sprite.Group()

# Only adds a dot if it has a unique home.
def negate_repeat():
    exists = False
    for e in dots:
        if home == e.home or home == e.work:
            exists = True
            break
    if exists == False: return False
    else: return True

# Creates the initial sick person.
def random_sickness():
    while True:
        e = dots[random.randint(0,len(dots)-1)]
        if e.state == dot.immune: continue
        e.becomeSick()
        dot.Dot.unexposed_count -= 1
        break

# Creates the natural 5% immunity.
def random_immune():
    percent = int(len(dots)*0.05)
    for i in range(percent):
        e = dots[i]
        if e.state == dot.unexposed:
            e.becomeImmune()
            dot.Dot.unexposed_count -= 1

# Runs 80% chance of becoming infected.
def unexposed_to_infected(dot1):
    rng = random.randint(0,9)
    if rng > 1: dot1.becomeInfected()

# Runs 50% chance of becoming sick.
def infected_to_sick(dot1):
    rng = random.randint(0,9)
    if rng > 4: dot1.becomeSick()

# Runs 98% chance of becoming immune.
# Else, becoming dead.
def sick_to_immune_or_dead(dot1):
    rng = random.randint(0,99)
    if rng > 1: dot1.becomeImmune()
    else:       dot1.becomeDead()

# Runs a check to make sure the dot counters are not negative.
def check_counts():
    if dot.Dot.unexposed_count < 0: dot.Dot.unexposed_count = 0
    if dot.Dot.sick_count < 0: dot.Dot.sick_count = 0
    if dot.Dot.infected_count < 0: dot.Dot.infected_count = 0
    if dot.Dot.immune_count < 0: dot.Dot.immune_count = 0        

# Start of main code.

pygame.init()
screen = pygame.display.set_mode([750, 750])
timer  = pygame.time.Clock()

### Dot creation.

while len(dots) < 100:
    home = (random.randint(0,750),random.randint(0,750))
    work = (random.randint(0,750),random.randint(0,750))
    d = dot.Dot(home,work)
    if negate_repeat() is False:
        dots.append(d)
        sprites.add(d)
        
random_immune()
random_sickness()

### Visuals and Game Logistics

screen.fill((255,255,255))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()

    # Game logistics

    # Checks collision between sick and unexposed.
    # Runs 80% chance of contracting virus.
    for d1, d2 in itertools.combinations(dots, 2):
        if pygame.sprite.collide_circle(d1,d2):
            if (d1.state == dot.sick or d1.state == dot.infected) and d2.state == dot.unexposed:
                unexposed_to_infected(d2)
            if (d2.state == dot.sick or d2.state == dot.infected) and d1.state == dot.unexposed:
                unexposed_to_infected(d1)

    # Checks the state of the infected people.
    # If 5 days have passed, run 50% chance of becoming sick.
    # If 15 days have passed, become immune.
    for d in dots:
        if d.state == dot.infected:
            d.day += 1
            if d.day == 5*20:
                infected_to_sick(d)
            if d.day == 15*20:
                d.becomeImmune()
            if dot.Dot.infected_count < 0:
                dot.Dot.infected_count = 0

    # Checks the state of the sick people.
    # If 10 days have passed, run 98% chance of becoming immune.
    # Else, become dead.
    for d in dots:
        if d.state == dot.sick:
            d.day += 1
            if d.day == 10*20:
                sick_to_immune_or_dead(d)

    screen.fill((255, 255, 255))

    # Moves the position of the dot closer to its "work."
    for e in dots:
        if e.state != dot.sick:
            e.moveLine()
            e.update()

    sprites.draw(screen)

    pygame.display.flip()
    timer.tick(20)
    check_counts()

pygame.quit()

print("total: ",dot.Dot.total_count)
print("unexposed: ",dot.Dot.unexposed_count)
print("infected: ",dot.Dot.infected_count)
print("immune: ",dot.Dot.immune_count)
print("sick: ",dot.Dot.sick_count)
print("dead: ",dot.Dot.dead_count)
