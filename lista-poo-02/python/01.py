# 1. Um Circulo

class Circulo:
    def __init__(self):
        self.__raio = float

    def set_raio(self, v: float):
        self.__raio = v

    def get_raio(self) -> float:
        return self.__raio
    
    def calc_area(self) -> float:
        # pi * (raio²)
        return 3.14 * (self.__raio ** 2)

    def calc_circunferencia(self) -> float:
        # 2 * pi * raio
        return 2 * 3.14 * self.__raio
    

c1 = Circulo()
c1.set_raio(5)

print(f"Raio: {c1.get_raio()}, Área: {c1.calc_area():.2f}, Circunferência: {c1.calc_circunferencia():.2f}")

c1.set_raio(10)

print(f"Raio: {c1.get_raio()}, Área: {c1.calc_area():.2f}, Circunferência: {c1.calc_circunferencia():.2f}")
