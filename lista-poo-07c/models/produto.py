# classe Produto


class Produto:
    __id: int
    __descricao: str
    __preco: float
    __estoque: int
    __id_categoria: int

    def __init__(
        self, id: int, descricao: str, preco: float, estoque: int, id_categoria: int
    ):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def __str__(self) -> str:
        return f"id: {self.__id}, {self.__descricao}, {self.__preco}, {self.__estoque}"

    def to_json(self) -> dict:
        return {
            "id": self.get_id(),
            "descricao": self.get_descricao(),
            "preco": self.get_preco(),
            "estoque": self.get_estoque(),
            "id_categoria": self.get_id_categoria(),
        }

    def from_json(json: dict) -> object:
        return Produto(
            json["id"],
            json["descricao"],
            json["preco"],
            json["estoque"],
            json["id_categoria"],
        )

    def get_id(self) -> int:
        return self.__id

    def get_descricao(self) -> str:
        return self.__descricao

    def get_preco(self) -> float:
        return self.__preco

    def get_estoque(self) -> int:
        return self.__estoque

    def get_id_categoria(self) -> int:
        return self.__id_categoria

    def set_id(self, i: int) -> None:
        if i < 0:
            return
        self.__id = i

    def set_id_categoria(self, id_cat: int) -> None:
        if id_cat < 0:
            return
        self.__id_categoria = id_cat

    def set_descricao(self, n: str) -> None:
        if not n:
            return
        self.__descricao = n

    def set_preco(self, p: float) -> None:
        if p < 0:
            return
        self.__preco = p

    def set_estoque(self, q: int) -> None:
        if q < 0:
            return
        self.__estoque = q
