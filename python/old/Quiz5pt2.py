import turtle
import random
import bisect
from PIL import Image, ImageDraw

bob = turtle.Turtle()       # defined as global so that functions can see bob

def midpoint_displacement(start, end, roughness, vertical_displacement=None,
                          num_of_iterations=16):
    if vertical_displacement is None:
        vertical_displacement = (start[1]+end[1])/2
    points = [start, end]
    iteration = 1
    while iteration <= num_of_iterations:
        points_tup = tuple(points)
        for i in range(len(points_tup)-1):
            midpoint = list(map(lambda x: (points_tup[i][x]+points_tup[i+1][x])/2,
                                [0, 1]))
            midpoint[1] += random.choice([-vertical_displacement,
                                          vertical_displacement])       
            bisect.insort(points, midpoint)
        vertical_displacement *= 2 ** (-roughness)
        iteration += 1
    return points


def draw_layers(layers, width, height, color_dict=None):
    if color_dict is None:
        color_dict = {'0': (195, 157, 224), '1': (158, 98, 204),
                      '2': (130, 79, 138), '3': (68, 28, 99), '4': (49, 7, 82),
                      '5': (23, 3, 38), '6': (240, 203, 163)}

    landscape = Image.new('RGBA', (width, height), color_dict[str(len(color_dict)-1)])
    turtle.begin_fill()
    landscape_draw = ImageDraw.Draw(landscape)
    turtle.goto(width, 0)
    turtle.goto(0,0)
    turtle.goto(0, height)
    turtle.end_fill()
    
        

    return landscape


def main():
    width = 1000  # Terrain width
    height = 500  # Terrain height

    turtle.setup(width,height,startx=None,starty=None)  # set turtle screen size
    turtle.bgcolor("#8899ee")                           # set background color

    bob.speed(0)                                        # draw as fast you can
    bob.penup()                                         # so that you don't draw a line yet
    bob.goto(-200,200)                                  # move pen to this location
    bob.fillcolor("yellow")                             # specify fill color
    bob.begin_fill()
    bob.circle(25)                                      # draw a filled circle of radius 25
    bob.end_fill()

 # Compute different layers of the landscape one at a time
    layer_1 = midpoint_displacement([250, 0], [width, 200], 1.4, 20, 10)
    layer_2 = midpoint_displacement([0, 180], [width, 80], 1.2, 30, 10)
    layer_3 = midpoint_displacement([0, 270], [width, 190], 1, 120, 9)
    layer_4 = midpoint_displacement([0, 350], [width, 320], 0.9, 250, 8)

    # note the drawing order is from "back to front"
    # "back" is the layer with highest y values
    draw_layers(layer_4, width, height, (158, 98, 204))
    draw_layers(layer_3, width, height, (130, 79, 138))
    draw_layers(layer_2, width, height, (68, 28, 99))
    draw_layers(layer_1, width, height, (49, 7, 82))

    # the next few lines is for adding text to our picture
    bob.goto(400,-220)
    bob.pencolor("yellow")
    bob.write("cse30, spring 2020", align="right", font=("Arial",10,"normal"))
    bob.goto(600,-300)   # move turtle offscreen

    turtle.done()

main()
