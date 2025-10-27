from cliente import Cliente
from pathlib import Path
import json


class ClienteDAO:
    objetos: list[Cliente] = []

    @staticmethod
    def inserir(obj: Cliente) -> None:
        ClienteDAO.objetos.append(obj)
        ClienteDAO.salvar()

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
                ClienteDAO.salvar()
                break

    @staticmethod
    def excluir(obj: Cliente) -> None:
        for i in range(len(ClienteDAO.objetos)):
            if ClienteDAO.objetos[i].get_id() == obj.get_id():
                del ClienteDAO.objetos[i]
                ClienteDAO.salvar()
                break

    @staticmethod
    def abrir() -> None:
        path = Path(__file__).parent / "json/clientes.json"
        if not path.exists():
            ClienteDAO.objetos = []
            return
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            ClienteDAO.objetos = []
            for item in data:
                if hasattr(Cliente, "from_dict"):
                    ClienteDAO.objetos.append(Cliente.from_dict(item))
                else:
                    ClienteDAO.objetos.append(Cliente(**item))
        except (json.JSONDecodeError, OSError):
            ClienteDAO.objetos = []

    @staticmethod
    def salvar() -> None:
        path = Path(__file__).parent / "json/clientes.json"
        data = []
        for obj in ClienteDAO.objetos:
            item = {
                "id": obj.get_id(),
                "nome": obj.get_nome(),
                "email": obj.get_email(),
                "fone": obj.get_fone(),
            }
            data.append(item)
        try:
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            pass
