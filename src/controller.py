import pygame
import front

def run_sim():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1024, 768))
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            front.update_frame(screen)
