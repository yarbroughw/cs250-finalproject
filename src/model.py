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
    def __init__(self, xmax, ymax, num_particles):
        self.xmax = xmax
        self.ymax = ymax
        self.particles = []

        for _ in range(num_particles):
            coord = (random.uniform(0, xmax), random.uniform(0, ymax))
            velocity = (random.random()*2 - 1.0,
                        random.random()*2 - 1.0)
            newparticle = Particle(coord, velocity)
            self.particles.append(newparticle)

    def step(self, detector=None):
        for p in self.particles:
            p.move()
            self.boundscheck(p)
        if detector:
            detector.check(self)

    def boundscheck(self, p):
        # TODO: debug, possibly
        if not (0 + p.radius) < p.coord[0] < (self.xmax - p.radius):
            p.velocity[0] *= -1
        if not (0 + p.radius) < p.coord[1] < (self.ymax - p.radius):
            p.velocity[1] *= -1
