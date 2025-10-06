# 2. Um Frete


class Frete:
    def __init__(self, d: float, p: float):
        self.d = d
        self.p = p

    def set_distancia(self, d: float):
        self.d = d

    def set_peso(self, p: float):
        self.p = p

    def get_distancia(self) -> float:
        return self.d

    def get_peso(self) -> float:
        return self.p

    def calc_frete(self) -> float:
        return 0.1 * self.d * self.p

    def __str__(self) -> str:
        return f"Frete Distancia {self.d}, Peso {self.p}"
