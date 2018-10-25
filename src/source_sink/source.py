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
