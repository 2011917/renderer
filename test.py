import math
import pygame

theta = 90
d = 1 / math.tan(math.radians(theta / 2))

width = 1920
height = 1080
a = width / height

file = "complicated.obj"

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

            if parts[0] == 'v':
                x, y, z = parts[1], parts[2], parts[3]
                verticies.append([float(x), float(y), float(z) + 5])

            elif parts[0] == 'f':
                # 2. Safety Check: Make sure it actually has 3 indices
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
        # 3. Safety Check: Ensure the index exists before looking it up
        if triangle[0]-1 < len(verticies) and triangle[1]-1 < len(verticies) and triangle[2]-1 < len(verticies):
            trianglecoords = [
                verticies[triangle[0] - 1], 
                verticies[triangle[1] - 1], 
                verticies[triangle[2] - 1]
            ]

            pixels = project(trianglecoords)

            # 4. THE FIX: Added ', 1' to draw hollow wireframes instead of giant solid blobs!
            pygame.draw.polygon(screen, (255, 255, 255), pixels, 1)

pygame.init()
screen = pygame.display.set_mode((width, height))
running = True

clock = pygame.time.Clock()

# File loaded once outside the loop (Great job!)
verticies, triangles = readobj(file)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    projerctobj(verticies, triangles)

    pygame.display.flip()