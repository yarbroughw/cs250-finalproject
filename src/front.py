import pygame
import sys
import model
import controller

# Color of non-colliding circles
blue = (138, 255, 255)
# Color of colliding circles
orange = (255, 170, 51)


def draw_circ(circle, color)
    '''A nice wrapper for pygame's ugly-ass draw syntax. '''
    pygame.gfxdraw.filled_circle(screen, c.coord[0], c.coord[1], c.radius, color)

def update_frame(screen):
    # Draw the background
    screen.fill((255, 255, 255))
    
    # Draw all of the circles
    for c in controller.world:
        #Are we colliding? If so, change the color
        if c.collide is False:
            draw_circ(c, blue)
        else:
            draw_circ(c, orange)

    # Update the screen
    pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        update_frame(screen)

