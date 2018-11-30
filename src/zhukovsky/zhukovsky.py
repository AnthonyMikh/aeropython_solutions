from typing import Callable

def zhukovsky(c: complex) -> Callable[[complex], complex]:
    def inner(z: complex) -> complex:
        return z + (c*c / z)
    return inner

def zhukovsky_real(c: complex) -> Callable[[complex], complex]:
    def inner(z: complex) -> complex:
        return (z + (c*c / z)).real
    return inner

def zhukovsky_imag(c: complex) -> Callable[[complex], complex]:
    def inner(z: complex) -> complex:
        return (z + (c*c / z)).imag
    return inner
