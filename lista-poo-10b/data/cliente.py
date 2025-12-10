# classe ClienteDAO
from pathlib import Path
from models.cliente import Cliente
from .base_dao import BaseDAO


class ClienteDAO(BaseDAO[Cliente]):
    path = Path(__file__).parent / "json/clientes.json"
    objetos: list[Cliente] = []
    model = Cliente
