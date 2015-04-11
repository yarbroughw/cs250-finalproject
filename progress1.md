# Progress Report I

## Project Structure

So far, our the design of our project involves several Python modules:

- `model.py`, which contains:
    * a `particle` class with x, y, and z coordinates as well as a velocity
      vector, and
    * a `world` class with x, y, z boundaries, a list of particles, `move`
      functions for each particle, and a master `step` function for updating
      all of the particles in the world.
- `collision.py`, which contains the octree implementation, the brute-force
  implementation, and a basic collision check primitive function, and
- `frontend.py`, which uses an `SDL` dependency to render the contents of
  `model.py` to the screen. This module also contains the `main()` function,
  which itself contains an event loop with calls to the `model` and `collision`
  modules.

So far, the basic structure of the model module has been implemented, as well
as some basic SDL usage. The collision module has yet to be implemented, though
we have designed its overall structure.

### `model.py`

The `model` module is quite simple, and involves a list of particles with a
fixed radius. This allows the primitive collision check in `collision.py` to
simply check for overlapping radii, without attempting to check for colliding
pixels (as would be necessary with a more complex shape). Collision with the
boundaries of the World space is accomplished by simply reflecting the vector
of a shape if that shapes coordinates lie outside of the World’s
boundaries after a call to `world.move(particle)`. `world.step()` calls
`world.move(particle)` over every particle in the `world` instance’s
list of particles. We intend to keep the `model` module as lean as possible, to
focus on the content of the `collision` module and the algorithms implemented
therein.

### `frontend.py`
The `frontend` module will handle rendering of objects described in `model`. We
are loosely following a model-view-controller (MVC) architecture, where the
`view` is `frontend.py`. In order to handle rendering of assets, we use the
Simple DirectMedia Layer API (SDL), which is essentially a cross-platform
wrapper for OpenGL and some basic functions related to playing audio. In order
to access SDL through Python, we use the aptly named PySDL2, which provides
bindings for the library. Unfortunately, we ran into some difficulties setting
up the library. For one thing, documentation of PySDL2 is scarce, making the
initial setup a time consuming process of trial and error. In addition, certain
drivers (including those on Alden's laptop) have either buggy or
extremely outdated implementations of OpenGL, which further complicates the
development process. Since we will only be making use of fairly simple
graphics, we will likely avoid most compatibility issues.

### Next Steps
For the next project checkpoint, we hope to implement the collision module
completely, including the `colliding()` function, the brute-force collision
detection method, and the Octree collision detection method. This will allow us
time for extension and evaluation of the Octree implementation before the
project due date.

