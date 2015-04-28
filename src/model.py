import random
import numpy as np


class Particle:
    ''' simple wrapper for coordinate and velocity '''
    def __init__(self, coord, velocity):
        self.coord = np.array(coord)
        self.velocity = np.array(velocity)
        self.radius = 10
        self.collide = False

    def move(self):
        self.coord += self.velocity


class World:
    def __init__(self, xmax, ymax, size):
        self.xmax = xmax
        self.ymax = ymax
        self.particles = []

        for _ in range(size):
            coord = (random.randint(0, xmax), random.randint(0, ymax))
            velocity = (random.random(), random.random())
            newparticle = Particle(coord, velocity)
            self.particles.append(newparticle)

    def step(self):
        for p in self.particles:
            p.move()
