# 3. Um Conversor Decimal-Binario


class Conversor:
    def __init__(self, num: int):
        self.num = num

    def set_numero(self, num: int):
        self.num = num

    def get_numero(self) -> int:
        return self.num

    def dec_bin(self) -> str:
        # Converte um número decimal para binário
        if self.num == 0:
            return "0"
        # pegamos o resto da divisao por 2
        # dividindo o número por 2 até 0
        n = self.num
        binario = ""
        while n > 0:
            binario = str(n % 2) + binario
            n = n // 2
        return binario

    def __str__(self) -> str:
        return f"Conversor Número {self.num}, Binário {self.dec_bin()}"
