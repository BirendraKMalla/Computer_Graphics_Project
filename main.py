import pygame
import time
import math
from bresenham import bresenham

width,height=1280,720
background_color = (0,0,0)

#startize line properties
rotating_line = True
x_origin = 50
y_origin = height - 50
length = 150

angle = 0
speed = 1
direction = 1

firing = False
fire_speed = 20



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
            if event.key == pygame.K_SPACE:
                firing = True
                firing_angle = math.radians(angle)
                shot_x2 = int(x_origin + length * math.cos(firing_angle))
                shot_y2 = int(y_origin - length * math.sin(firing_angle))
                shot_x1 = x_origin
                shot_y1 = y_origin

    #clear the screen for eaach frame
    screen.fill(background_color)
    
    #rotation logic
    if(rotating_line):
        angle += speed * direction
        if(angle >= 90):
            angle=90
            direction = -1
        elif angle <= 0:
            angle=0
            direction = 1

        rad = math.radians(angle)
        aim_x = int(x_origin + length * 0.7 * math.cos(rad)) 
        aim_y = int(y_origin - length * 0.7 * math.sin(rad))
        
    #line firing logic
    if(firing):
        shot_x1 += int(fire_speed * math.cos(firing_angle))
        shot_y1 -= int(fire_speed * math.sin(firing_angle))
        shot_x2 += int(fire_speed * math.cos(firing_angle))
        shot_y2 -= int(fire_speed * math.sin(firing_angle))
        # stop when off screen
        if shot_x1 > width or shot_y1 < 0:
            firing = False
            shot_x2 = int(x_origin + length * math.cos(firing_angle)) 
            shot_y2 = int(y_origin - length * math.sin(firing_angle))
            



    #sets pixels on the screen
    if(rotating_line):
        points = bresenham(x_origin, y_origin, aim_x, aim_y)
        for p in points:
            screen.set_at(p, (255,255,255))

    if(firing):
        points = bresenham(shot_x1, shot_y1, shot_x2, shot_y2)
        for p in points:
            screen.set_at(p, (255,255,255))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()