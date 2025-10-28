# classe CategoriaDAO
import json
from pathlib import Path
from models.categoria import Categoria
from dao.base_dao import BaseDAO


class CategoriaDAO(BaseDAO[Categoria]):
    _path = Path(__file__).parent / "json/categorias.json"
    _objetos: list[Categoria] = []

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
                if hasattr(Categoria, "from_dict"):
                    cls._objetos.append(Categoria.from_dict(item))
                else:
                    cls._objetos.append(Categoria(**item))
        except (json.JSONDecodeError, OSError):
            cls._objetos = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for cat in cls._objetos:
            item = {
                "id": cat.get_id(),
                "descricao": cat.get_descricao(),
            }
            data.append(item)
        try:
            with cls._path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass
