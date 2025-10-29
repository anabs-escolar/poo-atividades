# Classe Pessoa
from datetime import datetime


class Pessoa:
    __id: int
    __nome: str
    __nascimento: datetime

    def __init__(self, id: int, nome: str, nascimento: datetime) -> None:
        self.__id = id
        self.__nome = nome
        self.__nascimento = nascimento

    def __str__(self) -> str:
        return f"id: {self.id}, nome: {self.nome}, nascimento: {self.nascimento}"
        
    
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_nascimento(self) -> datetime:
        return self.__nascimento

    
    def set_id(self, id: int) -> None:
        self.__id = id

        
    def set_nome(self, nome: str) -> None:
        self.__nome = nome
        
    def set_nascimento(self, nascimento: datetime) -> None:
        self.__nascimento = nascimento