from .cliente import Cliente
from pathlib import Path
import json

class ClienteDAO:
    objetos: list[Cliente] = []

    @staticmethod
    def inserir(obj: Cliente) -> None:
        ClienteDAO.objetos.append(obj)

    @staticmethod
    def listar() -> list[Cliente]:
        return ClienteDAO.objetos

    @staticmethod
    def listar_id(id: int) -> Cliente | None:
        for obj in ClienteDAO.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @staticmethod
    def atualizar(obj: Cliente) -> None:
        for i in range(len(ClienteDAO.objetos)):
            if ClienteDAO.objetos[i].get_id() == obj.get_id():
                ClienteDAO.objetos[i] = obj
                break

    @staticmethod
    def excluir(obj: Cliente) -> None:
        for i in range(len(ClienteDAO.objetos)):
            if ClienteDAO.objetos[i].get_id() == obj.get_id():
                del ClienteDAO.objetos[i]
                break

    @staticmethod
    def abrir() -> None:
        path = Path(__file__).parent / "clientes.json"
        ClienteDAO.objetos = []
        if not path.exists():
            return
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            return

        if not isinstance(data, list):
            return

        for item in data:
            if not isinstance(item, dict):
                continue
            # Prefer a from_dict classmethod if available, otherwise try constructor with kwargs
            if hasattr(Cliente, "from_dict") and callable(getattr(Cliente, "from_dict")):
                try:
                    obj = Cliente.from_dict(item)
                except Exception:
                    continue
            else:
                try:
                    obj = Cliente(**item)
                except Exception:
                    continue
            ClienteDAO.objetos.append(obj)

    @staticmethod
    def salvar() -> None:
        path = Path(__file__).parent / "clientes.json"
        data = []
        for obj in ClienteDAO.objetos:
            item = {
                "id": obj.get_id(),
                "nome": obj.get_nome(),
                "email": obj.get_email(),
                "fone": obj.get_fone()
            }
            data.append(item)
        try:
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass