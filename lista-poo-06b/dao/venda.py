# classe VendaDAO
import json
from pathlib import Path
from ..models.venda import Venda
from ..dao.base_dao import BaseDAO


class VendaDAO(BaseDAO[Venda]):
    _path = Path(__file__).parent / "json/vendas.json"
    _objetos: list[Venda] = []

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
                if hasattr(Venda, "from_dict"):
                    cls._objetos.append(Venda.from_dict(item))
                else:
                    cls._objetos.append(Venda(**item))
        except (json.JSONDecodeError, OSError):
            cls._objetos = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for ven in cls._objetos:
            item = {
                "id": ven.get_id(),
                "data": ven.get_data(),
                "carrinho": ven.get_carrinho(),
                "total": ven.get_total(),
                "id_cliente": ven.get_id_cliente(),
            }
            data.append(item)
        try:
            with cls._path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass
