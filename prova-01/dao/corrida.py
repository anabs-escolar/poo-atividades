import json
from pathlib import Path
from base import BaseDAO
from models import Corrida

class CorridaDAO(BaseDAO[Corrida]):
    __path: str = Path(__file__).parent / "json/corrida.json"
    __objetos: list[Corrida] = []

    @classmethod
    def salvar(cls) -> None:
        data = []
        for i in cls.__objetos:
            item = {
                "id": i.get_id(),
                "id_pessoa": i.get_id_pessoa(),
                "data": i.get_data(),
                "distancia": i.get_distancia(),
                "tempo": i.get_tempo(), 
            }
            data.append(item)
        
        with cls.__path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)