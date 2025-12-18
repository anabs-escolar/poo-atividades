# classe Retangulo e Quadrado
import math


class Retangulo:
    b: float
    h: float

    def __init__(self, b: float, h: float):
        self.b = b
        self.h = h

    def get_base(self) -> float:
        return self.b

    def get_altura(self) -> float:
        return self.h

    def calc_area(self) -> float:
        return self.b * self.h

    def calc_diagonal(self) -> float:
        return math.sqrt(self.b**2 + self.h**2)

    def __str__(self) -> str:
        return f"Base: {self.b}, Altura: {self.h}"


class Quadrado(Retangulo):

    def __init__(self, l: float) -> None:
        self.b = l
        self.h = l

    def __str__(self) -> str:
        return f"Lado: {self.b}"


def main():
    print(" --- Retangulo e Quadrado --- ")
    print("Digite os altura e base do retângulo.")
    h = float(input("Altura: "))
    b = float(input("Base: "))

    r1 = Retangulo(b, h)
    print(r1)
    print(f"Area: {r1.calc_area()}")
    print(f"Diagonal: {r1.calc_diagonal()}")

    print("Digite o lado do quadrado.")
    l = float(input("Lado: "))
    q1 = Quadrado(l)
    print(q1)
    print(f"Area: {q1.calc_area()}")
    print(f"Diagonal: {q1.calc_diagonal()}")


main()
