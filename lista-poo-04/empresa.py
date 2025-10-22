from __future__ import annotations


# 3. Uma empresa
class Cliente:
    def __init__(self, nome: str, cpf: str, limite: float, socio: Cliente) -> None:
        self.nome = nome
        self.cpf = cpf
        self.limite = limite
        self.socio = socio

    def set_socio(self, c: Cliente) -> None:
        self.socio = c

    def get_limite(self) -> float:
        return self.limite

    def __str__(self) -> str:
        return self.nome


class Empresa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.__clientes: list[Cliente] = []

    def inserir(self, c: Cliente) -> None:
        self.__clientes.append(c)

    def listar(self) -> list[Cliente]:
        return self.__clientes

    def __str__(self) -> str:
        return self.nome
