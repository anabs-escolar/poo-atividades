class ContaBancaria:
    def __init__(self, titular: str, numero: str, saldo: float):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor: float):
        if valor <= 0:
            return "Valor inválido"
        
        self.saldo += valor
        return f"Depositado R$ {valor:.2f}"

    def sacar(self, valor: float):
        if valor > self.saldo:
            return "Saldo insuficiente"
        
        self.saldo -= valor
        return f"Sacado R$ {valor:.2f}"


c1 = ContaBancaria("Zé", "12345-6", 1000.0)
print(c1.depositar(500))
print(c1.sacar(200))
print(f"Saldo atual: R$ {c1.saldo:.2f}")