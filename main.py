import math
import pygame

triangle = [[0, 2, 5], [-2, -2, 5], [-2, 2, 5]]
triangle1 = [[1, 3, 5], [0, 2, 5], [-2, -2, 5]] 

theta = 90
d = 1 / math.tan(math.radians(theta / 2))

width = 1920
height = 1080
a = width / height

file="square.obj"

def readobj(infile):
    verticies = []

    triangles = []

    with open(infile, 'r') as file:
        for line in file.readlines():
            if line[0] == 'v':
                # 1. Clean off the trailing newline character (\n)
                cleaned_line = line.strip()

                # 2. Split by any amount of consecutive whitespace
                parts = cleaned_line.split()

                # 3. Double-check that it's a vertex line and unpack the coordinates
                if parts and parts[0] == 'v':
                    x, y, z = parts[1], parts[2], parts[3]
                    verticies.append([float(x), float(y), float(z)])

            if line[0] == 'f':
                # 1. Clean off the trailing newline character (\n)
                cleaned_line = line.strip()

                # 2. Split by any amount of consecutive whitespace
                parts = cleaned_line.split()

                # 3. Double-check that it's a vertex line and unpack the coordinates
                if parts and parts[0] == 'f':
                    a, b, c = parts[1], parts[2], parts[3]
                    triangles.append([int(a), int(b), int(c)])


    print(verticies)
    print(triangles)

    return verticies, triangles


def project(coords):
    pixels = []

    for point in coords:
        print(point)

        x = point[0]
        y = point[1]
        z = point[2]
        xprojected = (x * d) / (z * a)
        yprojected = (y * d) / z

        print(xprojected, yprojected)

        xpixel = ((xprojected + 1) / 2) * width
        ypixel = ((yprojected + 1) / 2) * height

        pixels.append((xpixel, ypixel))
        print(xpixel, ypixel)

    return pixels


def projerctobj(verticies, triangles):

    for triangle in triangles:

        trianglecoords=[verticies[triangle[0] - 1], verticies[triangle[1] - 1], verticies[triangle[2] - 1]]

        pixels = project(trianglecoords)

        pygame.draw.polygon(screen, (255, 255, 255), pixels)


   
pygame.init()
screen = pygame.display.set_mode((width, height))
running = True

clock = pygame.time.Clock()


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    verticies, triangles = readobj(file)
    projerctobj(verticies, triangles)

    
    

    pygame.display.flip()
