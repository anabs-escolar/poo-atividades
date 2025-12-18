# Figura 3D, Cubo e Esfera
from abc import ABC, abstractmethod
import math


class Figura3D:

    @abstractmethod
    def get_volume(self):
        pass


class Cubo(Figura3D):
    lado: float

    def __init__(self, lado: float):
        self.lado = lado

    def get_volume(self) -> float:
        return self.lado**3


class Esfera(Figura3D):
    raio: float

    def __init__(self, raio: float):
        self.raio = raio

    def get_volume(self):
        return (4 / 3) * math.pi * self.raio**3


def main():
    print(" --- Figuras 3D --- ")

    lado = float(input("Informe o lado do cubo: "))
    cubo = Cubo(lado)
    print(f"Volume do cubo: {cubo.get_volume():.2f}")

    raio = float(input("\nInforme o raio da esfera: "))
    esfera = Esfera(raio)
    print(f"Volume da esfera: {esfera.get_volume():.2f}")


main()
