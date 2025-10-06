# 3. Uma conta bancária

class ContaBancaria:
    def __init__(self):
        self.__titular = str
        self.__numero = str
        self.__saldo = float

    # Métodos setters
    def set_titular(self, t: str):
        self.__titular = t
    
    def set_numero(self, n: str):
        self.__numero = n
    
    def set_saldo(self, s: float):
        self.__saldo = s
    
    # Métodos getters
    def get_titular(self) -> str:
        return self.__titular
    
    def get_numero(self) -> str:
        return self.__numero
    
    def get_saldo(self) -> float:
        return self.__saldo
    

    def depositar(self, v: float) -> str:
        if v <= 0:
            return "Valor inválido"
        
        self.__saldo += v
        return f"Depositado R$ {v:.2f}"

    def sacar(self, v: float) -> str:
        if v > self.__saldo:
            return "Saldo insuficiente"
        
        self.__saldo -= v
        return f"Sacado R$ {v:.2f}"

c1 = ContaBancaria()
c1.set_titular("Zé")
c1.set_numero("12345-6")
c1.set_saldo(1000.0)

print(c1.depositar(500))
print(c1.sacar(200))
print(f"Saldo atual: R$ {c1.get_saldo():.2f}")