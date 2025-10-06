# 4. Uma Equação do Segundo Grau


class Equacao:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def set_a(self, value: float):
        self.a = value

    def get_b(self):
        return self.b

    def set_b(self, value: float):
        self.b = value

    def get_c(self):
        return self.c

    def set_c(self, value: float):
        self.c = value

    def delta(self) -> float:
        # b² - 4ac
        return self.b**2 - 4 * self.a * self.c

    def tem_raizes_reais(self) -> bool:
        return self.delta() >= 0

    def raiz_1(self) -> float | None:
        if not self.tem_raizes_reais():
            return None
        d = self.delta()
        r1 = (-self.b + d**0.5) / (2 * self.a)
        return r1

    def raiz_2(self) -> float | None:
        if not self.tem_raizes_reais():
            return None
        d = self.delta()
        r2 = (-self.b - d**0.5) / (2 * self.a)
        return r2

    def __str__(self) -> str:
        return f"Equação a = {self.a}, b = {self.b}, c = {self.c}"
