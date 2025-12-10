# class Categoria


class Categoria:
    __id: int
    __descricao: str

    def __init__(self, id: int, descricao: str):
        self.set_id(id)
        self.set_descricao(descricao)

    def __str__(self) -> str:
        return f"id: {self.__id}, descrição: {self.__descricao}"

    def to_json(self) -> dict:
        return {
            "id": self.get_id(),
            "descricao": self.get_descricao(),
        }

    @staticmethod
    def from_json(json: dict) -> object:
        return Categoria(
            json["id"],
            json["descricao"],
        )

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def get_id(self) -> int:
        return self.__id

    def get_descricao(self) -> str:
        return self.__descricao
