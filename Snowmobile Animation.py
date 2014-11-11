# Lab 8 - Snowmobile Animation

import pygame
import random

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0,  64,   4)
RED      = ( 255,   0,   0)
MIDNIGHT = (   0,  10,  64)
STAR     = ( 252, 252, 136)
GRAY     = ( 158, 186, 182)
ORANGE   = ( 247, 147,   7)

color_list = [BLACK,GREEN,MIDNIGHT,STAR,RED,ORANGE]

# Pygame StartUp, Window Sizing, Clock Set
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ice Bridge")
clock = pygame.time.Clock()

# Variables
snow_list = []
for i in range(200):
    x = random.randrange(-300, 700)
    y = random.randrange(-300, 500)
    snow_list.append([x, y])
star_list = []
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 450)
    star_list.append([x, y])
x_sled_move = 300
y_sled_move = 450

# Functions
def drawSnowmobile(x_sled, y_sled, color):
        pygame.draw.polygon(
            screen,
            GRAY,
            [[x_sled - 5, y_sled - 18],
             [x_sled + 25,y_sled - 10],
             [x_sled + 20, y_sled - 55]],
            0)
        pygame.draw.rect(
            screen,
            color,
            [x_sled, y_sled, 10, 6], 0)
        pygame.draw.line(
            screen,
            BLACK,
            [x_sled - 20, y_sled + 6],
            [x_sled + 25, y_sled + 6], 
            6)
        pygame.draw.line(
            screen,
            BLACK,
            [x_sled - 23, y_sled + 2],
            [x_sled - 20, y_sled + 6], 
            6)
        pygame.draw.polygon(
            screen,
            GRAY,
            [[x_sled + 10, y_sled],
            [x_sled + 10, y_sled - 20],
            [x_sled + 75, y_sled],
            [x_sled + 80, y_sled + 5],
            [x_sled + 75, y_sled + 8],
            [x_sled + 40, y_sled + 8],
            ],0)        
        pygame.draw.polygon(
            screen, 
            color,
            [[x_sled, y_sled],
             [x_sled - 10, y_sled - 20],
             [x_sled, y_sled - 30],
             [x_sled + 20, y_sled - 30],
             [x_sled + 25, y_sled - 25],
             [x_sled + 75, y_sled - 25],
             [x_sled + 80, y_sled - 20],
             [x_sled + 25, y_sled]],
            0)
        
# Loop until the user clicks the close button.
done = False
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # --- Drawing code should go here
    screen.fill(MIDNIGHT)
    # Draw Snowflakes
    # Process each snow flake in the list
    for i in range(len(star_list)):
        pygame.draw.circle(screen, STAR, star_list[i], 1)
    pygame.draw.line(screen, GREEN, [0, 400],[710,395],15)      
    for i in range(len(snow_list)):
     
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
     
        # Move the snow flake down one pixel
        snow_list[i][1] += 5
        snow_list[i][0] += 6
        
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 500:
              # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
              # Give it a new x position
            x = random.randrange(-500, 700)
            snow_list[i][0] = x   
    # Draws Ice  
    pygame.draw.rect(screen, WHITE, [0, 400, 700, 100])
    # Draws Snowmobile
    drawSnowmobile(x_sled_move,y_sled_move, RED)
    x_sled_move -= 3
    if x_sled_move < -90:
        x_sled_move = 700
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()