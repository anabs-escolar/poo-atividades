# 1. Um Bingo
import random

class Bingo:
    def __init__(self, numBolas: int):
        self.__numBolas = numBolas
        self.__bolas = []

    def proximo(self) -> int:
        if len(self.__bolas) == self.__numBolas:
            return -1

        num = random.randint(1, self.__numBolas)
        while num in self.__bolas:
            num = random.randint(1, self.__numBolas)

        self.__bolas.append(num)
        return num

    def sorteados(self) -> list[int]:
        return self.__bolas
    


bingo = Bingo(10)
print("Números sorteados:")
for _ in range(12):  # Tenta sortear mais do que o número de bolas
    numero = bingo.proximo()
    if numero == -1:
        print("Todos os números já foram sorteados.")
        break
    print(numero)
print("Lista de números sorteados:", sorted(bingo.sorteados()))
  # Ordena para melhor visualização
