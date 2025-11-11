# DAO Base
import json
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Tipo Generico
Model = TypeVar("Model")


class BaseDAO(ABC, Generic[Model]):
    path: str
    objetos: list[Model] = []
    model: object

    @classmethod
    def inserir(cls, obj: Model) -> None:
        id = 0
        for i in cls.objetos:
            if i.get_id() > id:
                id = i.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list:
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Model | None:
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Model) -> None:
        for i in range(len(cls.objetos)):
            if cls.objetos[i].get_id() == obj.get_id():
                cls.objetos[i] = obj
                cls.salvar()
                break

    @classmethod
    def excluir(cls, obj: Model) -> None:
        for i in range(len(cls.objetos)):
            if cls.objetos[i].get_id() == obj.get_id():
                del cls.objetos[i]
                cls.salvar()
                break

    @classmethod
    def abrir(cls) -> None:
        if not cls.path.exists():
            cls.objetos = []
            return
        try:
            with cls.path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            cls.objetos = []
            for item in data:
                cls.objetos.append(cls.model.from_json(item))
        except (json.JSONDecodeError, OSError):
            cls.objetos = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for i in cls.objetos:
            item = i.to_json()
            data.append(item)
        try:
            with cls.path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass
