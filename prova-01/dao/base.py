import json
from typing import Generic, TypeVar


Model = TypeVar("Model")


class BaseDAO(Generic[Model]):
    __path: str
    __objetos: list[Model] = []

    @classmethod
    def inserir(cls, obj: Model) -> None:
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Model]:
        return cls.__objetos
    
    @classmethod
    def abrir(cls) -> None:
        if not cls.__path.exists():
            return None
        
        with cls.__path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for i in data:
            if hasattr(Model, "from_dict"):
                cls.__objetos.append(Model.from_dict(i))
            else: 
                cls.__objetos.append(Model(**i))                
            
    @classmethod
    def salvar() -> None:
        pass