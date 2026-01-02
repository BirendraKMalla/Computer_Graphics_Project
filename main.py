import pygame
import math
from bresenham import bresenham
from rotation import rotation

#-----------------------------------------
#--------Constants------------------------
#-----------------------------------------

width, height = 1280, 720
background_color = (0, 0, 0)

# line properties
rotating_line = True
x_origin = width // 2
y_origin = height - 50
length = 100
x_end = x_origin + length
y_end = y_origin

angle = 0
rotation_speed = 1.5

# shot coordinates (needed before loop)
shots = []

#fired arrow properties
fire_speed = 10
firing_angle = 0
fired_arrow_length = 20
aim_x = x_end
aim_y = y_end

#-------------------------------------
#-----------functions-----------------
#-------------------------------------

def new_arrow(firing_angle):
    # NEW SHOT
    start_x = aim_x
    start_y = aim_y
    
    # Calculate the tail of the arrow/needle so it looks like a line
    end_x = int(start_x + fired_arrow_length * math.cos(firing_angle))
    end_y = int(start_y - fired_arrow_length * math.sin(firing_angle))
    shots.append({
        "x1": aim_x,
        "y1": aim_y,
        "x2": end_x,
        "y2": end_y,
        "angle": firing_angle
    })

def draw_aim_line(x_origin, y_origin, aim_x, aim_y):
    for p in bresenham(x_origin, y_origin, aim_x, aim_y):
        screen.set_at(p, (255, 255, 255))

def draw_fired_lines():
    for shot in shots[:]:
        dx = int(fire_speed * math.cos(shot["angle"]))
        dy = int(fire_speed * math.sin(shot["angle"]))

        shot["x1"] += dx
        shot["y1"] -= dy
        shot["x2"] += dx
        shot["y2"] -= dy

        if shot["x1"] > width or shot["y1"] < 0 or shot["x1"] <= 0:
            shots.remove(shot)
            continue

        draw_aim_line(shot["x1"], shot["y1"], shot["x2"], shot["y2"])


# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:
    #handles events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #creates new arrow if user presses space button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                new_arrow(math.radians(angle))

    screen.fill(background_color)

    #handle inputs
    #logic to manually control the anlge of line (needle)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        angle += rotation_speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        angle -= rotation_speed

    # clamp angle between 0 and 180
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180

    # rotation logic
    rad = math.radians(angle)
    rotating_end_points = rotation(x_end, y_end, x_origin, y_origin, -rad)
    aim_x = int(rotating_end_points[0].round())
    aim_y = int(rotating_end_points[1].round())

    # draw aim line
    draw_aim_line(x_origin, y_origin, aim_x, aim_y)

    # draw the fired lines
    draw_fired_lines()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()