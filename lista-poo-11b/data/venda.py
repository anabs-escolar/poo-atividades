# classe VendaDAO
import json
from pathlib import Path
from models.venda import Venda
from .dao import DAO



class VendaDAO(DAO[Venda]):
    objetos: list[Venda] = []

    @classmethod
    def abrir(cls) -> None:
    arquivo = Path("json/vendas.json")
        if not arquivo.exists():
            cls.objetos = []
            return

        with arquivo.open("r", encoding="utf-8") as f:
            data = json.load(f)

        cls.objetos = [Venda.from_json(item) for item in data]

    @classmethod
    def salvar(cls) -> None:
    arquivo = Path("json/vendas.json")
        data = [obj.to_json() for obj in cls.objetos]

        with arquivo.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
