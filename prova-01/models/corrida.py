# classe Corrida
from datetime import datetime, timedelta

class Corrida:
    __id: int
    __id_pessoa: int
    __data: datetime
    __distancia: int
    __tempo: timedelta

    def __init__(self, id: int, id_pessoa: int, data: datetime, distancia: int, tempo: timedelta) -> None:
        self.__id = id
        self.__id_pessoa = id_pessoa
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo

    def __str__(self) -> str:
        return f"id: {self.id}, data: {self.data.strftime("%d/%m/%Y")}, distância: {self.distância}Km, tempo: {self.tempo}"
    
    def pace(self) -> float:
        t = self.__tempo.min
        d = self.__distancia
        return t/d


    def get_id(self) -> int:
        return self.__id

    def get_id_pessoa(self) -> int:
        return self.__id_pessoa

    def get_data(self) -> datetime:
        return self.__data

    def get_distancia(self) -> int:
        return self.__distancia
    
    def get_tempo(self) -> timedelta:
        return self.__tempo


    def set_id(self, id: int) -> None:
        self.__id = id
    
    def set_id_pessoa(self, id_p: int) -> None:
        self.__id_pessoa = id_p

    def set_data(self, data: datetime) -> None:
        self.__data = data
        
    def set_distancia(self, distancia: int) -> None:
        self.__distancia = distancia

    def set_tempo(self, tempo: timedelta) -> None:
        self.__tempo = tempo
