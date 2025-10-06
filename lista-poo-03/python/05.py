# 5. Uma Data


class Data:
    def __init__(self, dia: int, mes: int, ano: int):

        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 0:
            raise ValueError("Ano inválido")

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def get_dia(self) -> int:
        return self.dia

    def set_dia(self, dia: int):
        self.dia = dia

    def get_mes(self) -> int:
        return self.mes

    def set_mes(self, mes: int):
        self.mes = mes

    def get_ano(self) -> int:
        return self.ano

    def set_ano(self, ano: int):
        self.ano = ano

    def set_data(self, data: str):
        d, m, a = map(int, data.split("/"))

        if d < 1 or d > 31:
            raise ValueError("Dia inválido")
        if m < 1 or m > 12:
            raise ValueError("Mês inválido")
        if a < 0:
            raise ValueError("Ano inválido")

        self.dia = d
        self.mes = m
        self.ano = a

    def __str__(self) -> str:
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"
