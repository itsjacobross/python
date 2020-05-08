import turtle

def draw_square(corners, color):
    ''' draws a single square and fills with color.
        assumes corners is list of 4 tuples representing the corners. '''

    turtle.fillcolor( color )                   # specify fillcolor
    turtle.penup()                              # don't draw anything yet
    turtle.begin_fill()                         # start of shape to fill
    turtle.goto( corners[0][0], corners[0][1] ) # starting point of shape
    turtle.pendown()                            # start drawing
    for i in range(len(corners)):               # draw to each corner & back
        turtle.goto( corners[(i+1)%4][0], corners[(i+1)%4][1] )
    turtle.end_fill()                           # end of shape to fill

colors = [(255,0,0),        # red
          (0,255,0),        # green
          (0,0,255),        # blue
          (128,128,128),    # gray
          (132, 31,  1),    # rand1
          ( 21, 12,122),    # rand2
          (123, 41,232),    # rand3
          ( 32,121, 49)]    # rand4

pt1=(-100, 100)
pt2=( 100, 100)
pt3=( 100,-100)
pt4=(-100,-100)

square=[pt1,pt2,pt3,pt4]    # outermost square

turtle.setup()              # setup canvas using default params
turtle.colormode(255)       # colors are defined as triples of 0..255 each
turtle.speed(0)             # draw as fast as you can
bob = turtle.Turtle()       # create drawing turtle

draw_square(square, colors[0]) # draw init square

pt1=(-100, 75)
pt2=(75, 100)
pt3=(100, -75)
pt4=(-75, -100)  # reinit boxes

square=[pt1,pt2,pt3,pt4]

for i in range(1, 8):
    draw_square( square, colors[i] )
    newpt1 = (pt1[0]*pow(0.90,i),pt1[1]*pow(0.75,i))
    newpt2 = (pt2[0]*pow(0.75,i),pt2[1]*pow(0.90,i))
    newpt3 = (pt3[0]*pow(0.90,i),pt3[1]*pow(0.75,i))
    newpt4 = (pt4[0]*pow(0.75,i),pt4[1]*pow(0.90,i))
    square=[newpt1,newpt2,newpt3,newpt4]

ts = turtle.getscreen()

turtle.done()
