# clase Venda
from datetime import datetime


class Venda:
    __id: int
    __data: datetime
    __carrinho: bool
    __total: float
    __id_cliente: int

    def __init__(
        self, id: int, data: datetime, carrinho: bool, total: float, id_cliente: int
    ):
        self.set_id(id)
        self.set_data(data)
        self.set_carrinho(carrinho)
        self.set_total(total)
        self.set_id_cliente(id_cliente)

    def __str__(self) -> str:
        return f"id: {self.__id}, {self.__data}, {self.__carrinho}, {self.__total}, {self.__id_cliente}"

    def to_json(self) -> dict:
        return {
            "id": self.get_id(),
            "data": self.get_data().isoformat(),
            "carrinho": self.get_carrinho(),
            "total": self.get_total(),
            "id_cliente": self.get_id_cliente(),
        }

    @staticmethod
    def from_json(json: dict) -> object:
        return Venda(
            json["id"],
            datetime.fromisoformat(json.get("data")),
            json["carrinho"],
            json["total"],
            json["id_cliente"],
        )

    def get_id(self) -> int:
        return self.__id

    def get_data(self) -> datetime:
        return self.__data

    def get_carrinho(self) -> bool:
        return self.__carrinho

    def get_total(self) -> float:
        return self.__total

    def get_id_cliente(self) -> int:
        return self.__id_cliente

    def set_id(self, i: int) -> None:
        if i < 0:
            return
        self.__id = i

    def set_data(self, d: datetime) -> None:
        self.__data = d

    def set_carrinho(self, c: bool) -> None:
        self.__carrinho = c

    def set_total(self, t: float) -> None:
        if t < 0:
            return
        self.__total = t

    def set_id_cliente(self, id_c: int) -> None:
        self.__id_cliente = id_c
