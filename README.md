# CS250 Final Project
Authors: Willem Yarbrough & Alden Page

## Project Proposal

### Background
Collision detection is an important component of any simulation software, and is
vital for such applications as game design, robotics, and physics simulations.
However, for a large number of objects in a simulation, collision detection can
be a very computationally expensive process. The naive, brute-force solution of
checking every pair of objects in the scene to see if they collide is a O(n^2)
algorithm that will not scale well for large numbers of entities.

A better solution is to use a tree-based data structure to partition the
simulation space into portions. This allows for the ignoring of distant pairs of
entities in the simulation that could not possibly be colliding, effectively
cutting down the number of pairs to check.  In a 2D space, this is accomplished
with a "quadtree", in which each node has either 0 or 4 children. The quadtree
divides the simulation space into quadrants. Similarly, for a 3D space, an
"octree" is used to divide the space into eight discrete spaces.

### Project Goal
Our final project will be an attempt to implement a basic, simple 3D physics
simulation in Python, and design a collision detection module for this engine.
This module will first use a brute-force collision detection algorithm, which
will be evaluated based on its performance (i.e., latency over number of
objects).  We will then proceed by improving this collision detection technique
using the octree data structure, which will be evaluated in the same manner.

Once this stage of the project is complete, we intend to improve on the
Octree implementation in some way. Some initial ideas for improvements are:

- **Variable partitioning.** Octrees typically divide the simulation space into
  exact halves. However, if our objects are clustered at one area in the
  space, this may result in an unbalanced tree. To combat this, the Octree could
  divide the space such that the resultant spaces have even numbers of
  entites.
- **Automatically balancing octrees.** Find a way to implement an Octree analog to
  the Red-Black Tree balancing technique. This may be an alternative to the
  previous idea, as it accomplishes the same goal. Thus, if time is available,
  both techniques could be implemented and evaluated.

Our implementation will be submitted together with analysis of our results, in
the form of mathematical analysis of the Octree algorithm and our improvement to
it, as well as experimental evaluations that support our claims.
