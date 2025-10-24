
class Cliente:
    __id: int
    __nome: str
    __email: str
    __fone: str

    def __init__(self, id: int, n: str, e: str, f: str):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__fone = f

    def __str__(self) -> str:
        return f"id: {self.id}, {self.nome}, {self.email}, {self.fone}"

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_fone(self) -> str:
        return self.__fone

    def set_nome(self, n: str) -> None:
        self.__nome = n 

    def set_email(self, e: str) -> None:
        self.__email = e

    def set_fone(self, f: str) -> None:
        self.__fone = f
