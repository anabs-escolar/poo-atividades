# classe Produto


class Produto:
    __id: int
    __descricao: str
    __preco: float
    __estoque: int
    __id_categoria: int

    def __init__(self, id: int, descricao: str, preco: float, estoque: int):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque

    def __str__(self) -> str:
        return f"id: {self.__id}, {self.__descricao}, {self.__preco}, {self.__estoque}"

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
