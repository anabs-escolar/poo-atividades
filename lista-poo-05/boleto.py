from enum import Enum
from datetime import datetime

# 2. Um Boleto


class Pagamento(Enum):
    em_aberto = 0
    pago_parcial = 1
    pago = 2


class Boleto:
    cod_barras: str
    data_emissao: datetime
    data_vencimento: datetime
    valor_boleto: float
    valor_pago: float = 0.0
    situacao_pagamento: Pagamento

    def __init__(
        self, cod: str, emissao: datetime, venc: datetime, valor: float
    ) -> None:
        self.cod_barras = cod
        self.data_emissao = emissao
        self.data_vencimento = venc
        self.valor_boleto = float(valor)
        # Inicia Valor Pago e Situacao
        self.valor_pago = float(0)
        self.situacao_pagamento = self.situacao()

    def pagar(self, valor_pago: float) -> None:
        if valor_pago < 0:
            raise ValueError("valor_pago não pode ser negativo")
        # soma o pagamento recebido ao total já pago
        self.valor_pago += valor_pago
        self.situacao_pagamento = self.situacao()

    def situacao(self) -> Pagamento:
        if self.valor_pago <= 0:
            return Pagamento.em_aberto
        if 0 < self.valor_pago < self.valor_boleto:
            return Pagamento.pago_parcial
        return Pagamento.pago

    def __str__(self):
        return f"{self.cod_barras}, Valor: {self.valor_boleto}, Valor Pago: {self.valor_pago}"
