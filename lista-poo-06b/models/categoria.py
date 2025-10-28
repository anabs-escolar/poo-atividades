# class Categoria


class Categoria:
    __id: int
    __descricao: str

    def __init__(self, id: int, descricao: str):
        self.__id = id
        self.__descricao = descricao

    def __str__(self) -> str:
        return f"id: {self.__id}, descrição: {self.__descricao}"

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def get_id(self) -> int:
        return self.__id

    def get_descricao(self) -> str:
        return self.__descricao
