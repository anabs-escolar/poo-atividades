from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class DAO(ABC, Generic[T]):
    
    objetos: list[T] = []

    @classmethod
    def inserir(cls, obj: T) -> None:
        novo_id = 0
        for i in cls.objetos:
            if i.get_id() > novo_id:
                novo_id = i.get_id()

        obj.set_id(novo_id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[T]:
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> T | None:
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: T) -> None:
        for i in range(len(cls.objetos)):
            if cls.objetos[i].get_id() == obj.get_id():
                cls.objetos[i] = obj
                cls.salvar()
                return

    @classmethod
    def excluir(cls, obj: T) -> None:
        cls.objetos = [i for i in cls.objetos if i.get_id() != obj.get_id()]
        cls.salvar()

    @classmethod
    @abstractmethod
    def abrir(cls) -> None:
        pass

    @classmethod
    @abstractmethod
    def salvar(cls) -> None:
        pass
