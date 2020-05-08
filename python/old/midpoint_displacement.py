import random
import bisect

VERTICES = [(-1,0,0), (1,0,0), (0,1,0)]

TRIANGLES = [(0,1,2)]

def midpoint_displacement(pt1, pt2, pt3, level):
    points = [pt1, pt2, pt3]
    points_tup = tuple(points)
    midpoint_A = list(map(lambda x: (points_tup[0][x]+points_tup[1][x])/2,[0, 1, 2]))
    midpoint_B = list(map(lambda x: (points_tup[1][x]+points_tup[2][x])/2,[0, 1 ,2]))
    midpoint_C = list(map(lambda x: (points_tup[2][x]+points_tup[0][x])/2,[0, 1, 2]))
    print(midpoint_A, midpoint_B, midpoint_C)

    if level == 0:
        #Displace the midpoints here
        VERTICES.append(tuple(midpoint_A))
        VERTICES.append(tuple(midpoint_B))
        VERTICES.append(tuple(midpoint_C))
        return

    else:
        triangle_tuple = (len(VERTICES)-3, len(VERTICES)-2, len(VERTICES)-1)
        TRIANGLES.append(triangle_tuple)
        midpoint_displacement(midpoint_A, midpoint_B, midpoint_C, level-1)
        midpoint_displacement(midpoint_A, midpoint_C, pt1, level-1)
        midpoint_displacement(midpoint_A, midpoint_B, pt2, level-1)
        midpoint_displacement(midpoint_B, midpoint_C, pt3, level-1)

    return points

midpoint_displacement(VERTICES[0],VERTICES[1],VERTICES[2],1)
print("Vertices:",VERTICES)
print("Triangles:", TRIANGLES)
