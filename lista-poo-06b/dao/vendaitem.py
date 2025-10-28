# classe VendaItemDAO
import json
from pathlib import Path
from ..models.vendaitem import VendaItem
from ..dao.base_dao import BaseDAO


class VendaItemDAO(BaseDAO[VendaItem]):
    _path = Path(__file__).parent / "json/vendaitens.json"
    _objetos: list[VendaItem] = []

    @classmethod
    def abrir(cls) -> None:
        if not cls._path.exists():
            cls._objetos = []
            return
        try:
            with cls._path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            cls._objetos = []
            for item in data:
                if hasattr(VendaItem, "from_dict"):
                    cls._objetos.append(VendaItem.from_dict(item))
                else:
                    cls._objetos.append(VendaItem(**item))
        except (json.JSONDecodeError, OSError):
            cls._objetos = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for vi in cls._objetos:
            item = {
                "id": vi.get_id(),
                "qtd": vi.get_qtd(),
                "preco": vi.get_preco(),
                "id_venda": vi.get_id_venda(),
                "id_produto": vi.get_id_produto(),
            }
            data.append(item)
        try:
            with cls._path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass
