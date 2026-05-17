import math
import pygame

triangle = [[0, 2, 5], [-2, -2, 5], [-2, 2, 5]]

theta = 90
d = 1 / math.tan(math.radians(theta / 2))

width = 1920
height = 1080
a = width / height


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

    projected = project(triangle)
    pygame.draw.polygon(screen, (255, 255, 255), projected)

    pygame.display.flip()
