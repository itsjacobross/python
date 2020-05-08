# Simple pygame program to move a dot from point A to point B

# sound clip: beep-07.wav is from
# https://www.soundjay.com/beep-sounds-1.html


# Import and initialize the pygame library
import pygame
import dot

# Set up the drawing window
#pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen = pygame.display.set_mode([600, 600])
timer  = pygame.time.Clock()
#effect = pygame.mixer.Sound('vinyl.wav')  # set up the sound clip

# create a dot object
d1 = dot.Dot((255,500), (250,0))
d2 = dot.Dot((0,250), (500,250))

dots=[d1,d2]
sprites = pygame.sprite.Group()
sprites.add(d1)
sprites.add(d2)

# Fill the background with white
screen.fill((255, 255, 255))

#Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()

    if pygame.sprite.collide_rect(d1,d2):
        d1.stop()
        d2.stop()

    screen.fill((255, 255, 255))

    # Move each dot on the list
    for e in dots:
        #pygame.draw.circle( screen, e.color, e.gps, e.size )
        #e.move()
        #e.moveManhattan()
        e.update()
        e.moveLine()
        #print(e.rect.x,e.rect.y)
        #effect.play()   # play the sound clip each time the dot moves

    sprites.draw(screen)

    # Flip the display
    pygame.display.flip()
    timer.tick(4)       # slowed down to 1fps so beep is not too annoying

# Done! Time to quit.
pygame.quit()
