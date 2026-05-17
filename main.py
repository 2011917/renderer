import math
import pygame

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
            cleaned_line = line.strip()
            parts = cleaned_line.split()

            # 1. Safety Check: Skip empty lines so the parser doesn't crash!
            if not parts:
                continue

            if  parts[0] == 'v':
                x, y, z = parts[1], parts[2], parts[3]
                verticies.append([float(x), float(y), float(z)+5])



                # 3. Double-check that it's a vertex line and unpack the coordinates
            elif parts and parts[0] == 'f':
                if len(parts) >= 4:
                    a, b, c = parts[1], parts[2], parts[3]
                    triangles.append([int(a), int(b), int(c)])

    return verticies, triangles


def project(coords):
    pixels = []

    for point in coords:

        x = point[0]
        y = point[1]
        z = point[2]

        # Prevent math errors if a point ever reaches exactly Z=0
        if z == 0:
            z = 0.0001

        xprojected = (x * d) / (z * a)
        yprojected = (y * d) / z


        xpixel = ((xprojected + 1) / 2) * width
        ypixel = ((yprojected + 1) / 2) * height

        pixels.append((xpixel, ypixel))

    return pixels


def projerctobj(verticies, triangles):

    for triangle in triangles:

        if triangle[0]-1 < len(verticies) and triangle[1]-1 < len(verticies) and triangle[2]-1 < len(verticies):
                    trianglecoords = [
                        verticies[triangle[0] - 1], 
                        verticies[triangle[1] - 1], 
                        verticies[triangle[2] - 1]
                    ]
        pixels = project(trianglecoords)

        pygame.draw.polygon(screen, (255, 255, 255), pixels,1)


   
pygame.init()
screen = pygame.display.set_mode((width, height))
running = True

clock = pygame.time.Clock()


verticies, triangles = readobj(file)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    projerctobj(verticies, triangles)

    pygame.display.flip()
