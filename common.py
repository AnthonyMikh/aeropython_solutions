#!/usr/bin/env python
# coding: utf-8

import math
import numpy as np
from matplotlib import pyplot as plt

from typing import NamedTuple, Tuple

Grid = Tuple['numpy.ndarray', 'numpy.ndarray']

class Coords(NamedTuple):
    x: float
    y: float

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

class Rect:
    def __init__(self, x_start: float, x_end: float, y_start: float, y_end: float):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end

    def __str__(self) -> str:
        return 'Rect: x = {} .. {}, y = {} .. {}'            .format(self.x_start, self.x_end, self.y_start, self.y_end)
    
    @property
    def width(self) -> float:
        return self.x_end - self.x_start
    
    @property
    def height(self) -> float:
        return self.y_end - self.y_start
    
    @property
    def span_x(self) -> (float, float):
        return (self.x_start, self.x_end)
    
    @property
    def span_y(self) -> (float, float):
        return (self.y_start, self.y_end)

    def make_grid(self, N: int) -> ('numpy.ndarray', 'numpy.ndarray'):
        xs = np.linspace(self.x_start, self.x_end, N)
        ys = np.linspace(self.y_start, self.y_end, N)
        return np.meshgrid(xs, ys)


def setup_fig(rect: Rect, size: int,             *, xlabel: str = 'x', ylabel: str = 'y',             label_size: int = 16):
    plt.figure(figsize = (size, rect.height / rect.width * size))
    plt.xlabel(xlabel, fontsize = label_size)
    plt.ylabel(ylabel, fontsize = label_size)
    plt.xlim(*rect.span_x)
    plt.ylim(*rect.span_y)

def hypot(x0, y0, x1, y1):
    return (x1 - x0)**2 + (y0 - y1)**2


class Source:
    def __init__(self, x: float, y: float, strength: float):
        self.x = x
        self.y = y
        self.strength = strength
    
    @property
    def coords(self) -> Coords:
        return Coords(self.x, self.y)
    
    def __str__(self) -> str:
        return f'Source: ({self.x}, {self.y}), strength = {self.strength}'
    
    def velocity(self, grid: Grid) -> Grid:
        x, y = self.coords
        X, Y = grid
        coeff = self.strength / (2.0 * math.pi * hypot(x, y, X, Y))
        u = coeff * (X - x)
        v = coeff * (Y - y)
        return (u, v)
    
    def potential(self, grid: Grid) -> 'numpy.ndarray':
        X, Y = grid
        return self.strength / (2.0 * math.pi) * np.arctan2(Y - self.y, X - self.x)