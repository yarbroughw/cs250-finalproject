import numpy as np


class Particle:
    def __init__(self, coord, velocity):
        self.coord = np.array(coord)
        self.velocity = np.array(velocity)
        self.radius = 10


def move(p):
    p.coord += p.velocity


def step(particles):
    for p in particles:
        move(p)
