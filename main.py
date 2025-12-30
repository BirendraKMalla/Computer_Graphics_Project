import pygame
import math
from bresenham import bresenham

width,height=1280,720

#initialize line properties
x_origin = 50
y_origin = height - 50
length = 150

angle = 0
speed = 1
direction = 1

firing = False
fire_speed = 10

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not firing:
                firing = True
                firing_angle = math.radians(angle)
                x_tip = int(x_origin + length * math.cos(firing_angle))
                y_tip = int(y_origin - length * math.sin(firing_angle))
                initial_x = x_origin
                initial_y = y_origin

    #clear the screen for eaach frame
    screen.fill((0, 0, 0))
    
    #rotation logic
    if(not firing):
        angle += speed * direction
        if(angle >= 90):
            angle=90
            direction = -1
        elif angle <= 0:
            angle=0
            direction = 1

        rad = math.radians(angle)
        x_tip = int(x_origin + length * math.cos(rad)) 
        y_tip = int(y_origin - length * math.sin(rad))
        
    #line firing logic
    elif(firing):
        x_tip += int(fire_speed * math.cos(firing_angle))
        y_tip -= int(fire_speed * math.sin(firing_angle))
        initial_x += int(fire_speed * math.cos(firing_angle))
        initial_y -= int(fire_speed * math.sin(firing_angle))
        # stop when off screen
        if initial_x > width or initial_y < 0:
            firing = False
            



    #sets pixels on the screen
    if(not firing):
        points = bresenham(x_origin, y_origin, x_tip, y_tip)
        for p in points:
            screen.set_at(p, (255,255,255))
    else:
        points = bresenham(initial_x, initial_y, x_tip, y_tip)
        for p in points:
            screen.set_at(p, (255,255,255))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()