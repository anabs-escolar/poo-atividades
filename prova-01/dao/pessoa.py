import json
from pathlib import Path
from base import BaseDAO
from models import Pessoa

class PessoaDAO(BaseDAO[Pessoa]):
    __path: str = Path(__file__).parent / "json/pessoa.json"
    __objetos: list[Pessoa] = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for i in cls.__objetos:
            item = {
                "id": i.get_id(),
                "nome": i.get_nome(),
                "nascimento": i.get_nascimento(),
            }
            data.append(item)
        
        with cls.__path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)