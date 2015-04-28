import pygame
from pygame import gfxdraw
import sys
import model
import controller

background = (201, 201, 201)
# Color of non-colliding circles
blue = (138, 255, 255)
# Color of colliding circles
orange = (255, 170, 51)

def draw_circ(circle, color, screen):
    '''A nice wrapper for pygame's ugly-ass draw syntax. '''
    gfxdraw.filled_circle(screen, int(circle.coord[0]), int(circle.coord[1]),
        circle.radius, color)

def update_frame(world, screen):
    '''Draw everything onto the screen.'''
    # Draw the background
    screen.fill(background)
    
    # Draw all of the circles
    for c in world.particles:
        #Are we colliding? If so, change the color
        if c.collide is False:
            draw_circ(c, blue, screen)
        else:
            draw_circ(c, orange, screen)

    # Update the screen
    pygame.display.update()
