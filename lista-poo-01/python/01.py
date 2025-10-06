class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        # pi*(raio²)
        return 3.14 * (self.raio ** 2)

    def circunferencia(self):
        # 2*pi*raio
        return 2 * 3.14 * self.raio


c1 = Circulo(5)
print("Área do círculo:", c1.area())
print("Circunferência do círculo:", c1.circunferencia())