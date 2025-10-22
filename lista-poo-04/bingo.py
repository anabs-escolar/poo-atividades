# 1. Um Bingo
import random


class Bingo:
    def __init__(self, numBolas: int):
        self.numBolas = numBolas
        self.bolas = []

    def proximo(self) -> int:
        if len(self.bolas) < self.numBolas:
            prox_num = random.randint(1, self.numBolas)
            while prox_num in self.bolas:
                prox_num = random.randint(1, self.numBolas)
            self.bolas.append(prox_num)
            return prox_num
        return -1

    def sorteados(self) -> list:
        return self.bolas
