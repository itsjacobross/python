import math
import turtle
import random
import bisect

# For Program 1, you need to replace the code between the tags # BEGIN and # END with your code. 
# Your code should generate the VERTICES and TRIANGLES using your recursive "midpoint_displacement" function. 
# This setup is optimized for points values generated in the range -1.00 to 1.00.
# You may need the adjust the value of FOV to generate points with higher ranges.

#=====================================================================
VERTICES = []
TRIANGLES = []
start_1 = [-1,0,0]
start_2 = [1,0,0]
start_3 = [0,1,0]

def midpoint_displacement(pt1, pt2, pt3, level=0, roughness=1.4, vertical_displacement=1):
    points = [pt1, pt2, pt3]
    points_tup = tuple(points)
    midpoint_A = list(map(lambda x: (points_tup[0][x]+points_tup[1][x])/2,[0, 1, 2]))
    midpoint_B = list(map(lambda x: (points_tup[1][x]+points_tup[2][x])/2,[0, 1 ,2]))
    midpoint_C = list(map(lambda x: (points_tup[2][x]+points_tup[0][x])/2,[0, 1, 2]))

    if level == 0:
        for [x,y,z] in VERTICES:
            if pt1[0] == x and pt1[1] == y:
                pt1 = [x,y,z]
                break
            elif pt1 == start_1 or pt1 == start_2 or pt1 == start_3:
                break
        else:
            pt1[2] += random.choice([-vertical_displacement, vertical_displacement])/2
        for [x,y,z] in VERTICES:
            if pt2[0] == x and pt2[1] == y:
                pt2 = [x,y,z]
                break
            elif pt2 == start_1 or pt2 == start_2 or pt2 == start_3:
                break
        else:
            pt2[2] += random.choice([-vertical_displacement, vertical_displacement])/2
        for [x,y,z] in VERTICES:
            if pt3[0] == x and pt3[1] == y:
                pt3 = [x,y,z]
                break
            elif pt3 == start_1 or pt3 == start_2 or pt3 == start_3:
                break
        else:
            pt3[2] += random.choice([-vertical_displacement, vertical_displacement])/2
        VERTICES.append(pt1)
        VERTICES.append(pt2)
        VERTICES.append(pt3)
        triangle_tuple = (len(VERTICES)-3, len(VERTICES)-2, len(VERTICES)-1)
        TRIANGLES.append(triangle_tuple)
        return

    else:
        new_vd = vertical_displacement * 1.5 ** (-roughness)
        midpoint_displacement(midpoint_A, midpoint_B, midpoint_C, level-1, vertical_displacement=new_vd)
        midpoint_displacement(midpoint_A, midpoint_C, pt1, level-1, vertical_displacement=new_vd)
        midpoint_displacement(midpoint_A, midpoint_B, pt2, level-1, vertical_displacement=new_vd)
        midpoint_displacement(midpoint_B, midpoint_C, pt3, level-1, vertical_displacement=new_vd)

    return points

midpoint_displacement(start_1, start_2, start_3, level=6)
print(VERTICES)

#=====================================================================
    
def transform(x, y, z, angle, tilt):
    #Animation control (around y-axis)
    s, c = math.sin(angle), math.cos(angle)
    x, y = x * c - y * s, x * s + y * c

    #Camera tilt  (around x-axis)
    s, c = math.sin(tilt), math.cos(tilt)
    z, y = z * c - y * s, z * s + y * c

    # Setting up View Parameters
    y += 5 #Fixed Distance from top # original at 5
    FOV = 2300 #Fixed Field of view
    f = FOV / y
    sx, sy = x * f, z * f
    return sx, sy

def main():
    # Create terrain using turtle
    terrain = turtle.Turtle()
    terrain.pencolor("blue")
    terrain.pensize(2)

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
            sx, sy = transform(x, y, z, angle, 0.4) #x,y,z,angle,0.25 #1.57 for topdown
            VERT2D.append((sx, sy))

        # Draw the terrain
        for triangle in TRIANGLES:
            points = []
            points.append(VERT2D[triangle[0]])
            points.append(VERT2D[triangle[1]])
            points.append(VERT2D[triangle[2]])

            # Draw the trangle
            terrain.goto(points[0][0], points[0][1])
            terrain.down()

            terrain.goto(points[1][0], points[1][1])
            terrain.goto(points[2][0], points[2][1])
            terrain.goto(points[0][0], points[0][1])
            terrain.up()

        # Update screen
        turtle.update()

        # Control the speed of animation
        angle += 0.01 #was 0.0005

if __name__ == "__main__":
    main()
