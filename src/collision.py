import numpy as np


class Node:
    def __init__(self):
        self.particles = []
        self.children = []


class Quadtree:
    def __init__(self):
        self.root = None
        self.splitAt = None

    def add(self, particle):
        pass

    def update(self, particle):
        pass


def colliding(p1, p2):
    ''' returns true if particles are colliding '''
    distance = np.linalg.norm(p1.coord - p2.coord)
    return p1.radius + p2.radius >= distance
