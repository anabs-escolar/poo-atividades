class Viagem:
    def __init__(self, distancia, tempo):
        # distancia = Km
        # tempo = horas:minutos
        self.distancia = distancia
        self.tempo = tempo
    
    def velocidade_media(self):
        horas, minutos = map(int, self.tempo.split(':'))
        horas += minutos / 60
        # velocidade média = distância / tempo
        return self.distancia / horas


v1 = Viagem(240, "4:00")
print(f"Distancia: {v1.distancia} Km, Tempo: {v1.tempo} h, Velocidade média: {v1.velocidade_media()} Km/h")

v2 = Viagem(150, "3:30")
print(f"Distancia: {v2.distancia} Km, Tempo: {v2.tempo} h, Velocidade média: {v2.velocidade_media()} Km/h")