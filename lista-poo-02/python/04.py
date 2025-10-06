# 4. Uma Entrada de Cinema

class EntradaCinema:
    def __init__(self):
        # dia ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
        self.__dia = str       
        # hora 24h 
        self.__hora = int

    def set_dia(self, d: str):
        self.__dia = d
    
    def set_hora(self, h: int):
        self.__hora = h
    

    def get_dia(self) -> str:
        return self.__dia
    
    def get_hora(self) -> int:
        return self.__hora
    

    def preco(self):
        horas = self.__hora
        dia = self.__dia
        valor = 0.0

        if dia in ["seg", "ter", "qui"]:
            valor = 16.0
        
        elif dia == "qua":
            valor = 8.0
        
        elif dia in ["sex", "sab", "dom"]:
            valor = 20.0
        
        if horas < 17 and not(dia == "qua"):
            valor += valor * 0.5

        return valor
    
    def meia_entrada(self):
        dia = self.__dia
        
        if dia == "qua":
            return self.preco()
    
        return self.preco() * 0.5