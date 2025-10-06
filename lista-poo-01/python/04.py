class EntradaCinema:
    def __init__(self, dia: str, hora: str):
        # dia ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
        self.dia = dia
        # hora 24h "HH:MM"
        self.hora = hora

    def preco(self):
        horas, minutos = map(int, self.hora.split(':'))
        valor = 0.0
        if self.dia in ["seg", "ter", "qui"]:
            valor = 16.0
        
        elif self.dia == "qua":
            valor = 8.0
        
        elif self.dia in ["sex", "sab", "dom"]:
            valor = 20.0
        
        if horas < 17 and not(self.dia == "qua"):
            valor += valor * 0.5

        return valor
    
    def meia_entrada(self):
        if self.dia == "qua":
            return self.preco()
    
        return self.preco() * 0.5


e1 = EntradaCinema("seg", "14:00")
print(f"Dia: {e1.dia}, Hora: {e1.hora}, Preço: R$ {e1.preco():.2f}, Meia-entrada: R$ {e1.meia_entrada():.2f}")

e2 = EntradaCinema("qua", "19:30")
print(f"Dia: {e2.dia}, Hora: {e2.hora}, Preço: R$ {e2.preco():.2f}, Meia-entrada: R$ {e2.meia_entrada():.2f}")

e3 = EntradaCinema("dom", "16:00")
print(f"Dia: {e3.dia}, Hora: {e3.hora}, Preço: R$ {e3.preco():.2f}, Meia-entrada: R$ {e3.meia_entrada():.2f}")
