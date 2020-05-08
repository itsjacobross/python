import math
import turtle

VERTICES = [(-1, 1, -1), ( 1, 1, -1), ( 1, -1, -1), (-1, -1, -1),
            (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1),
            (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1),
            (-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1),
            (1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1),
            (-1, 1, 1), (1, 1, 1), (1, -1, 1), (-1, -1, 1)]

SQUARES = [(0, 1, 2, 3),
           (4, 5, 6, 7),
           (8, 9, 10, 11),
           (12, 13, 14, 15),
           (16, 17, 18, 19),
           (20, 21, 22, 23)]

def transform(x, y, z, angle, tilt):
    #Animation control (around y-axis)
    s, c = math.sin(angle), math.cos(angle)
    x, y = x * c - y * s, x * s + y * c

    #Camera tilt  (around x-axis)
    s, c = math.sin(tilt), math.cos(tilt)
    z, y = z * c - y * s, z * s + y * c

    # Setting up View Parameters
    y += 5 #Fixed Distance from top
    FOV = 1000 #Fixed Field of view
    f = FOV / y
    sx, sy = x * f, z * f
    return sx, sy

def main():
    # Create terrain using turtle
    terrain = turtle.Turtle()
    terrain.pencolor("blue")
    terrain.pensize(2)

    height = 500
    width = 500
    turtle.screensize(height, width)

    # Turn off move time for instant drawing
    turtle.tracer(0, 0)
    terrain.up()
    angle = 0
    
    while True:
        # Clear the screen
        terrain.clear()
        
        # Transform the terrain
        VERT2D = []
        for vert3D in VERTICES:
            x, y, z = vert3D
            sx, sy = transform(x, y, z, angle, 0.25)
            VERT2D.append((sx, sy))

        # Draw the terrain
        for square in SQUARES:
            points = []
            points.append(VERT2D[square[0]])
            points.append(VERT2D[square[1]])
            points.append(VERT2D[square[2]])
            points.append(VERT2D[square[3]])
            print(points)

            terrain.goto(points[0][0], points[0][1])
            terrain.down()

            terrain.goto(points[1][0], points[1][1])
            terrain.goto(points[2][0], points[2][1])
            terrain.goto(points[3][0], points[3][1])
            terrain.goto(points[0][0], points[0][1])
            terrain.up()

        # Update screen
        turtle.update()

        # Control the speed of animation
        angle += 0.0005
        
if __name__ == "__main__":
    main()
