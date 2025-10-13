# 01. Um Paciente

from datetime import datetime

class Paciente:
    def __init__(self, n: str, c: str, t: str, nasc: datetime):
        self.nome = n
        self.cpf = c
        self.telefone = t
        self.nascimento = nasc

    def idade(self) -> str:
        hoje = datetime.now()
        idade = hoje.year - self.nascimento.year
        if (hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day):
            idade -= 1
        return f"{idade} anos"
        
