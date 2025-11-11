# classe CategoriaDAO
from pathlib import Path
from models.categoria import Categoria
from dao.base_dao import BaseDAO


class CategoriaDAO(BaseDAO[Categoria]):
    path = Path(__file__).parent / "json/categorias.json"
    objetos: list[Categoria] = []
    model = Categoria
