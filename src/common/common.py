#!/usr/bin/env python
# coding: utf-8

import math
import numpy as np
from matplotlib import pyplot as plt

from typing import NamedTuple, Tuple, List

Grid = Tuple['numpy.ndarray', 'numpy.ndarray']

class Coords(NamedTuple):
    x: float
    y: float

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

def unzip_coords(*coords) -> (List[float], List[float]):
    xs, ys = [], []
    for (x, y) in coords:
        xs.append(x)
        ys.append(y)
    return (xs, ys)

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

stream_params = {'density': 2, 'linewidth': 1, 'arrowsize': 2, 'arrowstyle': '->'}
scatter_params = {'color': '#CD2305', 's': 80, 'marker': 'o', 'linewidth': 0}

def streamplot_with(*args, override):
    params = stream_params.copy()
    params.update(override)
    plt.streamplot(*args, **params)

def scatter_with(*args, override):
    params = scatter_params.copy()
    params.update(override)
    plt.scatter(*args, **params)    

def hypot(x0, y0, x1, y1):
    return (x1 - x0)**2 + (y0 - y1)**2

def sum_pair(a, b):
    a0, a1 = a
    b0, b1 = b
    return (a0 + b0, a1 + b1)
