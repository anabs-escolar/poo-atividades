# DAO Base
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Tipo Generico
Model = TypeVar("T")


class BaseDAO(ABC, Generic[Model]):
    _path: str
    _objetos: list[Model] = []

    @classmethod
    def inserir(cls, obj: Model) -> None:
        cls._objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list:
        return cls._objetos

    @classmethod
    def listar_id(cls, id: int) -> Model | None:
        for obj in cls._objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Model) -> None:
        for i in range(len(cls._objetos)):
            if cls._objetos[i].get_id() == obj.get_id():
                cls._objetos[i] = obj
                cls.salvar()
                break

    @classmethod
    def excluir(cls, obj: Model) -> None:
        for i in range(len(cls._objetos)):
            if cls._objetos[i].get_id() == obj.get_id():
                del cls._objetos[i]
                cls.salvar()
                break

    @classmethod
    @abstractmethod
    def abrir() -> None:
        pass

    @classmethod
    @abstractmethod
    def salvar() -> None:
        pass
