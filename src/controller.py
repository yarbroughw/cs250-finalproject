import pygame
import front
import model

WIN_SIZE = (1024, 768)

def run_sim():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WIN_SIZE)
    world = model.World(WIN_SIZE[0], WIN_SIZE[1], 10)
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            front.update_frame(screen)
            world.step(None)
