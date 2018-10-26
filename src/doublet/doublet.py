class Doublet:
    def __init__(self, x: float, y: float, strength: float):
        self.x = x
        self.y = y
        self.strength = strength
    
    @property
    def coords(self) -> Coords:
        return Coords(self.x, self.y)
    
    def __str__(self) -> str:
        return f'Doublet: ({self.x}, {self.y}), strength = {self.strength}'
    
    def velocity(self, grid: Grid) -> Grid:
        x, y = self.coords
        X, Y = grid
        coeff = -self.strength/(2.0 * math.pi * hypot(x, y, X, Y)**2)
        u = ((X - x)**2 - (Y - y)**2) * coeff
        v = 2.0 * (X - x) * (Y - y) * coeff
        return (u, v)
    
    def potential(self, grid: Grid) -> 'numpy.ndarray':
        x, y = self.coords
        X, Y = grid
        return (-self.strength * (Y - y))/(2.0 * math.pi * hypot(x, y, X, Y))
