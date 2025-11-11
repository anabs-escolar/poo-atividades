# classe Cliente


class Cliente:
    __id: int
    __nome: str
    __email: str
    __senha: str
    __fone: str
    __is_admin: bool

    def __init__(
        self,
        id: int,
        nome: str,
        email: str,
        senha: str,
        fone: str,
        is_admin: bool = False,
    ):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_fone(fone)
        self.set_is_admin(is_admin)

    def __str__(self) -> str:
        return f"id: {self.__id}, {self.__nome}, {self.__email}, {self.__fone}"

    def to_json(self) -> dict:
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "email": self.get_email(),
            "senha": self.get_senha(),
            "fone": self.get_fone(),
            "is_admin": self.get_is_admin(),
        }

    @staticmethod
    def from_json(json: dict) -> object:
        return Cliente(
            json["id"],
            json["nome"],
            json["email"],
            json["senha"],
            json["fone"],
            json["is_admin"],
        )

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_senha(self) -> str:
        return self.__senha

    def get_fone(self) -> str:
        return self.__fone

    def get_is_admin(self) -> bool:
        return self.__is_admin

    def set_id(self, i: int) -> None:
        if i < 0:
            return
        self.__id = i

    def set_nome(self, n: str) -> None:
        if not n:
            return
        self.__nome = n

    def set_email(self, e: str) -> None:
        if not e:
            return
        self.__email = e

    def set_senha(self, s: str) -> None:
        if not s:
            return
        self.__senha = s

    def set_fone(self, f: str) -> None:
        if not f:
            return
        self.__fone = f

    def set_is_admin(self, is_admin: bool) -> None:
        self.__is_admin = is_admin
