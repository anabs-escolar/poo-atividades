# classe VendaDAO
from pathlib import Path
from models.venda import Venda
from .base_dao import BaseDAO


class VendaDAO(BaseDAO[Venda]):
    path = Path(__file__).parent / "json/vendas.json"
    objetos: list[Venda] = []
    model = Venda
