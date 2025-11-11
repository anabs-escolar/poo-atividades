# classe ClienteDAO
import json
from pathlib import Path
from models.cliente import Cliente
from dao.base_dao import BaseDAO


class ClienteDAO(BaseDAO[Cliente]):
    path = Path(__file__).parent / "json/clientes.json"
    objetos: list[Cliente] = []
    model = Cliente
