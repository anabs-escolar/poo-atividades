from datetime import datetime

# 1. Um Paciente


class Paciente:
    def __init__(self, n: str, c: str, t: str, nasc: datetime):
        self.nome = n
        self.cpf = c
        self.telefone = t
        self.nascimento = nasc

    def idade(self) -> str:
        hoje = datetime.today().date()
        nasc = self.nascimentod
        if isinstance(nasc, datetime):
            nasc = nasc.date()
        years = (
            hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
        )
        return nasc.strftime("%d/%m/%Y")

    def __str__(self) -> str:
        return self.nome
