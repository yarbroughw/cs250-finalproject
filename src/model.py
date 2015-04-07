
class Particle:
    def __init__(self, coord, velocity):
        self.coord = coord
        self.velocity = velocity


def move(particle):
    x, y, z = particle.coord
    dx, dy, dz = particle.velocity
    particle.coord = (x+dx, y+dy, z+dz)


def step(particles):
    for p in particles:
        move(p)
