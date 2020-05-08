import turtle

def drawC( x1,y1, x2,y2, color, level ):
        # My Code 
        if level == 0:
                turtle.goto(x1,y1)
                turtle.pendown()
                turtle.goto(x2,y2)
                turtle.penup()
        else:
                mx = (x1+x2+y1-y2)/2
                my = (x2+y1+y2-x1)/2
                drawC(x1,y1,mx,my,color,level-1)
                drawC(mx,my,x2,y2,color,level-1)


# main code follows:

turtle.setup()
turtle.shape("turtle")
turtle.colormode(255)
turtle.speed(10)
turtle.bgcolor("#008080")
turtle.width(4)
turtle.penup()

color=( 12, 50, 231)

drawC(0,-100,  0,100, color, 8)

turtle.done()
