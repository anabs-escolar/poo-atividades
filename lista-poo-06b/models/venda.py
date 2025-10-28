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
        self.__id = id
        self.__data = data
        self.__carrinho = carrinho
        self.__total = total
        self.__id_cliente = id_cliente

    def __str__(self) -> str:
        return f"id: {self.__id}, {self.__data}, {self.__carrinho}, {self.__total}, {self.__id_cliente}"

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
