import numpy as np
import itertools as it

P_LIMIT = 5


class Node:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.particles = []
        self.children = None

        # delimiters for space represented by this node
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.xmid = (self.xmin + self.xmax) // 2
        self.ymid = (self.ymin + self.ymax) // 2

    def add(self, particle):
        if not self.children:
            if len(self.particles) >= P_LIMIT:
                self.split()
                self.add(particle)
            else:
                self.particles.add(particle)
        else:
            quadrant = self.quadrant(particle)
            if quadrant < 0:
                self.particles.add(particle)
            else:
                self.children[quadrant].add(particle)

    def split(self):
        ''' creates child nodes for quadrants '''
        ul = Node(self.xmin, self.xmid, self.ymin, self.ymid)
        ur = Node(self.xmid, self.xmax, self.ymin, self.ymid)
        lr = Node(self.xmid, self.xmax, self.ymid, self.ymax)
        ll = Node(self.xmin, self.xmid, self.ymid, self.ymax)
        self.children = [ul, ur, lr, ll]

    def quadrant(self, particle):
        '''Returns index of quadrant for particle in children array.
           Returns -1 if particle straddles the line.
        '''

        if abs(particle.coord[0] - self.xmid) < particle.radius or \
           abs(particle.coord[1] - self.ymid) < particle.radius:
            return -1

        if 0 < particle.coord[0] < self.xmid:
            return 0 if 0 < particle.coord[1] < self.ymid else 3
        else:
            return 1 if 0 < particle.coord[1] < self.ymid else 2

    def hasColliding(self, p):
        for p2 in self.particles:
            if colliding(p, p2):
                return True
        return False


class Quadtree:
    def __init__(self, world):
        self.root = Node(0, world.xmax, 0, world.ymax)
        for particle in world.particles:
            self.add(particle)

    def add(self, particle):
        self.root.add(particle)

    def update(self, particle):
        pass


def colliding(p1, p2):
    ''' returns true if particles are colliding '''
    distance = np.linalg.norm(p1.coord - p2.coord)
    return p1.radius + p2.radius >= distance


class BasicDetector:
    def __init__(self):
        pass

    def check(self, world):
        ''' brute force, n^2 collision detection '''
        for p in world.particles:
            p.collide = False
        for (p1, p2) in it.combinations(world.particles, 2):
            if colliding(p1, p2):
                p1.collide = True
                p2.collide = True


class QuadtreeDetector:
    def __init__(self):
        pass

    def check(self, world):
        qt = Quadtree(self.world)
        for p in world.particles:
            p.collide = False
        for p in world.particles:
            current = qt.root
            while True:
                if current.hasColliding(p):
                    p.collide = True
                if current.children is not None:
                    current = current.children[qt.quadrant(p)]
                else:
                    break
