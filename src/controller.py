import sys
import pygame
import front
import model
import collision

WIN_SIZE = (1024, 768)

def run_sim(arg):
    detector = None
    if arg is 0:
        print("No collision detection enabled.")
    if arg is 1:
        print("Using brute force collision detection.")
        detector = collision.BasicDetector()
    if arg is 2:
        print("Using Quadtree collision detection.")
        detector = collision.QuadtreeDetector()

    pygame.init()
    # clock = pygame.time.Clock()
    world = model.World(WIN_SIZE[0], WIN_SIZE[1], 50)
    screen = pygame.display.set_mode(WIN_SIZE)
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        front.update_frame(world, screen)
        world.step(detector)
