# classe VendaItemDAO
import json
from pathlib import Path
from models.vendaitens import VendaItem
from .dao import DAO



class VendaItemDAO(DAO[VendaItem]):
    objetos: list[VendaItem] = []

    @classmethod
    def abrir(cls) -> None:
        arquivo = Path("json/clievendaitensntes.json")
        if not arquivo.exists():
            cls.objetos = []
            return

        with arquivo.open("r", encoding="utf-8") as f:
            data = json.load(f)

        cls.objetos = [VendaItem.from_json(item) for item in data]

    @classmethod
    def salvar(cls) -> None:
        arquivo = Path("json/vendaitens.json")
        data = [obj.to_json() for obj in cls.objetos]

        with arquivo.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
