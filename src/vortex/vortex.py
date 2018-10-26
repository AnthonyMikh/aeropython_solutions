class Vortex:
    def __init__(self, x, y, strength):
        self.x = x
        self.y = y
        self.strength = strength
    
    @property
    def coords(self) -> Coords:
        return Coords(self.x, self.y)
    
    def __str__(self) -> str:
        return f'Vortex: ({self.x}, {self.y}), strength = {self.strength}'
    
    def velocity(self, grid: Grid) -> Grid:
        x, y = self.coords
        X, Y = grid
        coeff = self.strength/(2.0 * math.pi * hypot(x, y, X, Y))
        u = +(Y - y) * coeff
        v = -(X - x) * coeff
        return (u, v)
    
    def potential(self, grid: Grid) -> 'numpy.ndarray':
        return self.strength/(4.0 * math.pi) * np.log(hypot(*self.coords, *grid))
