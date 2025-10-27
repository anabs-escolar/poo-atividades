class Cliente:
    __id: int
    __nome: str
    __email: str
    __fone: str

    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def __str__(self) -> str:
        return f"id: {self.__id}, {self.__nome}, {self.__email}, {self.__fone}"

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_fone(self) -> str:
        return self.__fone

    def set_nome(self, n: str) -> None:
        if not n:
            return
        self.__nome = n

    def set_email(self, e: str) -> None:
        if not e:
            return
        self.__email = e

    def set_fone(self, f: str) -> None:
        if not f:
            return
        self.__fone = f
