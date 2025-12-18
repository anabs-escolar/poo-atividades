# classe Frete e Frete Expresso


class Frete:
    distancia: float
    peso: float

    def __init__(self, d: float, p: float):
        self.distancia = d
        self.peso = p

    def valor_frete(self) -> float:
        return self.peso * self.distancia * 0.01

    def __str__(self) -> str:
        return f"Distância: {self.distancia} - Peso: {self.peso}"


class FreteExpresso(Frete):
    seguro: float

    def __init__(self, d: float, p: float, s: float):
        super().__init__(d, p)
        self.seguro = s

    def valor_frete(self):
        return super().valor_frete() * 2 + self.seguro * 0.01

    def __str__(self) -> str:
        return super().__str__() + f" - Seguro: {self.seguro}"


def main():
    print(" --- Frete --- ")
    print("Digite a distancia (Km) e peso da entrega (Kg).")
    d = float(input("Distancia (Km): "))
    p = float(input("Peso (Kg): "))

    f1 = Frete(d, p)
    print(f1)
    print(f"Valor do Frete: {f1.valor_frete()}")

    print(" --- Frete Expresso --- ")
    print("Digite a distancia (Km) e peso da entrega (Kg).")
    de = float(input("Distancia (Km): "))
    pe = float(input("Peso (Kg): "))
    se = float(input("Seguro (R$): "))
    fe = FreteExpresso(de, pe, se)
    print(fe)
    print(f"Valor do Frete: {fe.valor_frete()}")


main()
