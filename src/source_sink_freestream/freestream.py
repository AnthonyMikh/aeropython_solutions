#!/usr/bin/env python
# coding: utf-8

class Freestream:
    def __init__(self, vel_inf: float, angle: float = 0.0):
        if angle is not None and angle != 0.0:
            raise NotImplementedError
        self.vel_inf = vel_inf
    
    def potential(self, grid: Grid) -> 'numpy.ndarray':
        return self.vel_inf * grid[1]
    
    def velocity(self, grid: Grid) -> Grid:
        u = self.vel_inf * np.ones(grid[0].shape, dtype=float)
        v = np.zeros(grid[0].shape, dtype=float)
        return (u, v)
