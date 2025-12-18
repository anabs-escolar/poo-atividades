from .retangulo import Retangulo


class Quadrado(Retangulo):
    
    def __init__(self, l: float) -> None:
        self.b = l
        self.h = l

    def __str__(self) -> str:
        return f"Lado: {self.b}"