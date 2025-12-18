import math 

class Retangulo:
    b: float
    h: float

    def __init__(self, b: float, d: float)
        self.b = b
        self.h = h

    def get_base() -> float:
        return self.b

    def get_altura() -> float:
        return self.h

    def calc_area() -> float:
        return self.b * self.h

    def calc_diagonal() -> float:
        return math.sqrt(self.b**2 + self.h**2)
    
    def __str__(self) -> str:
        return f"Base: {self.b}, Altura: {self.h}"