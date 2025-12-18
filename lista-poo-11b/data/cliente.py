# classe ClienteDAO
import json
from pathlib import Path
from models.cliente import Cliente
from .dao import DAO



class ClienteDAO(DAO[Cliente]):
    objetos: list[Cliente] = []

    @classmethod
    def abrir(cls) -> None:
        arquivo = Path("json/clientes.json")
        if not arquivo.exists():
            cls.objetos = []
            return

        with arquivo.open("r", encoding="utf-8") as f:
            data = json.load(f)

        cls.objetos = [Cliente.from_json(item) for item in data]

    @classmethod
    def salvar(cls) -> None:
        arquivo = Path("json/clientes.json")
        data = [obj.to_json() for obj in cls.objetos]

        with arquivo.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
