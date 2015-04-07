
class Particle:
    ''' simple wrapper for coordinate and velocity '''
    def __init__(self, coord, velocity):
        self.coord = coord
        self.velocity = velocity


class World:
    def __init__(self, xmax, ymax, zmax):
        self.xmax = xmax
        self.ymax = ymax
        self.zmax = zmax
        self.particles = []

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
