# 2. Uma viagem

class Viagem:
    def __init__(self, ):
        self.__distancia = float    # Km
        self.__tempo = float        # Hora


    def set_distancia(self, d: float):
        self.__distancia = d

    def set_tempo(self, t: float):
        self.__tempo = t

    def get_distancia(self) -> float:
        return self.__distancia
    
    def get_tempo(self) -> float:
        return self.__tempo
    
    def velociade_media(self) -> float:
        # velocidade média = distância / tempo
        return self.__distancia / self.__tempo
    

v1 = Viagem()
v1.set_distancia(240)
v1.set_tempo(4.0)
print(f"Distancia: {v1.get_distancia()} Km, Tempo: {v1.get_tempo()} h, Velocidade média: {v1.velociade_media()} Km/h")

v1.set_distancia(150)
v1.set_tempo(3.5)
print(f"Distancia: {v1.get_distancia()} Km, Tempo: {v1.get_tempo()} h, Velocidade média: {v1.velociade_media()} Km/h")