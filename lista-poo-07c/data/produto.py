# classe ProdutoDAO
from pathlib import Path
from models.produto import Produto
from .base_dao import BaseDAO


class ProdutoDAO(BaseDAO[Produto]):
    path = Path(__file__).parent / "json/produtos.json"
    objetos: list[Produto] = []
    model = Produto
