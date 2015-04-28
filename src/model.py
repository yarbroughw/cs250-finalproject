import random


class Particle:
    ''' simple wrapper for coordinate and velocity '''
    def __init__(self, coord, velocity):
        self.coord = coord
        self.velocity = velocity


class World:
    def __init__(self, xmax, ymax, zmax, size):
        self.xmax = xmax
        self.ymax = ymax
        self.zmax = zmax
        self.particles = []

        for _ in range(size):
            coord = (random.randint(0, xmax),
                     random.randint(0, ymax),
                     random.randint(0, zmax))
            velocity = (1, 1, 1)
            newparticle = Particle(coord, velocity)
            self.particles.append(newparticle)

    def move(self, particle):
        x, y, z = particle.coord
        dx, dy, dz = particle.velocity
        x, y, z = (x+dx, y+dy, z+dz)

        # bounds checking
        if not 0 < x < self.xmax:
            particle.velocity = (dx*-1, dy, dz)
        if not 0 < y < self.ymax:
            particle.velocity = (dx, dy*-1, dz)
        if not 0 < z < self.zmax:
            particle.velocity = (dx, dy, dz*-1)

    def step(self, particles):
        for p in particles:
            self.move(p)
