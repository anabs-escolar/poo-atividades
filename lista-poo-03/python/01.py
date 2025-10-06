# 1. Um Retangulo


class Retangulo:
    def __init__(self, b: float, h: float):
        self.b = b
        self.h = h

    def set_base(self, b: float):
        self.b = b

    def set_altura(self, h: float):
        self.h = h

    def get_base(self) -> float:
        return self.b

    def get_altura(self) -> float:
        return self.h

    def calc_area(self) -> float:
        return self.b * self.h

    def calc_diagonal(self) -> float:
        # (b² + h²)¹/²
        return (self.b**2 + self.h**2) ** 0.5

    def __str__(self) -> str:
        return f"Retangulo Base {self.b}, Altura {self.h}"
