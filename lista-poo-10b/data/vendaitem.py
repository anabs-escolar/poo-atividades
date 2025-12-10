# classe VendaItemDAO
from pathlib import Path
from models.vendaitem import VendaItem
from .base_dao import BaseDAO


class VendaItemDAO(BaseDAO[VendaItem]):
    path = Path(__file__).parent / "json/vendaitens.json"
    objetos: list[VendaItem] = []
    model = VendaItem
