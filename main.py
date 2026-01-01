import pygame
import math
from bresenham import bresenham

width, height = 1280, 720
background_color = (0, 0, 0)

# line properties
rotating_line = True
x_origin = 50
y_origin = height - 50
length = 150

angle = 0
speed = 1
direction = 1

firing = False
fire_speed = 20

# shot coordinates (needed before loop)
firing_angle = 0

shots = []

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                firing_angle = math.radians(angle)

                # NEW SHOT (same variables you used, just stored)
                shots.append({
                    "x1": x_origin,
                    "y1": y_origin,
                    "x2": int(x_origin + length * math.cos(firing_angle)),
                    "y2": int(y_origin - length * math.sin(firing_angle)),
                    "angle": firing_angle
                })
            
    

    screen.fill(background_color)
    #logic to manually control the anlge of line (needle)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        angle += speed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        angle -= speed

    # clamp angle between 0 and 90
    if angle < 0:
        angle = 0
    elif angle > 90:
        angle = 90

    # rotation logic
    if rotating_line:
        # angle += speed * direction
        # if angle >= 90:
        #     angle = 90
        #     direction = -1
        # elif angle <= 0:
        #     angle = 0
        #     direction = 1
        rad = math.radians(angle)
        aim_x = int(x_origin + length * 0.7 * math.cos(rad))  #the scalar is for pointer length
        aim_y = int(y_origin - length * 0.7 * math.sin(rad))

    # firing logic
    if firing:
        dx = int(fire_speed * math.cos(firing_angle))
        dy = int(fire_speed * math.sin(firing_angle))

        shot_x1 += dx
        shot_y1 -= dy
        shot_x2 += dx
        shot_y2 -= dy

        if shot_x1 > width or shot_y1 < 0:
            firing = False
            shot_x1 = shot_y1 = 0
            shot_x2 = shot_y2 = 0

    # draw aim line
    if rotating_line:
        for p in bresenham(x_origin, y_origin, aim_x, aim_y):
            screen.set_at(p, (255, 255, 255))

    for shot in shots[:]:
        dx = int(fire_speed * math.cos(shot["angle"]))
        dy = int(fire_speed * math.sin(shot["angle"]))

        shot["x1"] += dx
        shot["y1"] -= dy
        shot["x2"] += dx
        shot["y2"] -= dy

        if shot["x1"] > width or shot["y1"] < 0:
            shots.remove(shot)
            continue

        for p in bresenham(shot["x1"], shot["y1"], shot["x2"], shot["y2"]):
            screen.set_at(p, (255, 255, 255))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
