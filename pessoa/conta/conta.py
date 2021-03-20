from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, value):
        if not isinstance(value, (int, float)):
            print('Valor da Agência precisa ser numérico')
            return

        self._agencia = value

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, value):
        if not isinstance(value, (int, float)):
            print('Valor da Conta precisa ser numérico')
            return

        self._conta = value

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, (int, float)):
            print('Valor da Saldo precisa ser numérico')
            return

        self._saldo = value

    def detalhes(self):
        print(f'Agencia: {self._agencia}')
        print(f'Conta: {self._conta}')
        print(f'Saldo: R${self.saldo:.2f}')
        print()

    def depositar(self, value):
        if not isinstance(value, (int, float)):
            print('Valor para depósito precisa ser numérico')
            return

        self.saldo += value
        self.detalhes()

    @abstractmethod
    def sacar(self, value):
        pass
