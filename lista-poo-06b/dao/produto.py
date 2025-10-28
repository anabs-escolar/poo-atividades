# classe ProdutoDAO
import json
from pathlib import Path
from ..models.produto import Produto
from ..dao.base_dao import BaseDAO


class ProdutoDAO(BaseDAO[Produto]):
    _path = Path(__file__).parent / "json/produtos.json"
    _objetos: list[Produto] = []

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
                if hasattr(Produto, "from_dict"):
                    cls._objetos.append(Produto.from_dict(item))
                else:
                    cls._objetos.append(Produto(**item))
        except (json.JSONDecodeError, OSError):
            cls._objetos = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for pro in cls._objetos:
            item = {
                "id": pro.get_id(),
                "descricao": pro.get_descricao(),
                "preco": pro.get_preco(),
                "estoque": pro.get_estoque(),
                "id_categoria": pro.get_id_categoria(),
            }
            data.append(item)
        try:
            with cls._path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass
