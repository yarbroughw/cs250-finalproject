import pygame
import sys
import model


def update_frame(screen):
    # Draw the background
    screen.fill((255, 255, 255))
    
    # Draw all of the circles
    for circle in controller.world:


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

