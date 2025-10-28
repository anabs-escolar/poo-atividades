# classe ClienteDAO
import json
from pathlib import Path
from models.cliente import Cliente
from dao.base_dao import BaseDAO


class ClienteDAO(BaseDAO[Cliente]):
    _path = Path(__file__).parent / "json/clientes.json"
    _objetos: list[Cliente] = []

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
                if hasattr(Cliente, "from_dict"):
                    cls._objetos.append(Cliente.from_dict(item))
                else:
                    cls._objetos.append(Cliente(**item))
        except (json.JSONDecodeError, OSError):
            cls._objetos = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for cli in cls._objetos:
            item = {
                "id": cli.get_id(),
                "nome": cli.get_nome(),
                "email": cli.get_email(),
                "fone": cli.get_fone(),
            }
            data.append(item)
        try:
            with cls._path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass
