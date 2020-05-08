# Simple pygame program to move a dot from point A to point B

# Import and initialize the pygame library
import pygame
import dot

# Set up the drawing window
pygame.init()
screen = pygame.display.set_mode([500, 500])
timer  = pygame.time.Clock()

# create a dot object
ptA = (10,10)
ptB = (300,400)
d = dot.Dot(ptA,ptB)

dots=[d]

#Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Move each dot on the list
    for e in dots:
        pygame.draw.circle( screen, e.color, e.gps, e.size )
        e.move()

    # Flip the display
    pygame.display.flip()
    timer.tick(120)

# Done! Time to quit.
pygame.quit()
