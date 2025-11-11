## classe VendaItem


class VendaItem:
    __id: int
    __qtd: int
    __preco: float
    __id_venda: int
    __id_produto: int

    def __init__(self, id: int, id_venda: int, id_produto: int, qtd: int, preco: float):
        self.__id = id
        self.__id_venda = id_venda
        self.__id_produto = id_produto
        self.__qtd = qtd
        self.__preco = preco

    def __str__(self) -> str:
        return f"id: {self.__id}, venda: {self.__id_venda}, produto: {self.__id_produto}, quantidade: {self.__qtd}, preco: {self.__preco}"

    def to_json(self) -> dict:
        return {
            "id": self.get_id(),
            "id_venda": self.get_id_venda(),
            "id_produto": self.get_id_produto(),
            "qtd": self.get_qtd(),
            "preco": self.get_preco(),
        }

    @staticmethod
    def from_json(json: dict) -> object:
        return VendaItem(
            json["id"],
            json["id_venda"],
            json["id_produto"],
            json["qtd"],
            json["preco"],
        )

    def get_id(self) -> int:
        return self.__id

    def get_id_venda(self) -> int:
        return self.__id_venda

    def get_id_produto(self) -> int:
        return self.__id_produto

    def get_qtd(self) -> int:
        return self.__qtd

    def get_preco(self) -> float:
        return self.__preco

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_id_venda(self, id_venda: int) -> None:
        self.__id_venda = id_venda

    def set_id_produto(self, id_produto: int) -> None:
        self.__id_produto = id_produto

    def set_qtd(self, qtd: int) -> None:
        self.__qtd = qtd

    def set_preco(self, preco: float) -> None:
        self.__preco = preco
