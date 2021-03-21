from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(agencia, conta, saldo=0):
        self._agencia = agencia 
        self._conta = conta 
        self._saldo = saldo 

    @property
    def agencia(self) -> object:
        return self._agencia 

    @property
    def conta(self) -> object:
        return self._conta 

    @property
    def saldo(self) -> object:
        return self._saldo 

    def depositar(self, valor):
        self._saldo += valor 
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia}'
              f'Conta: {self._conta}'
              f'Saldo: R${self._saldo:.2f}')
        print()

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo Insuficiente') 
            return 

        self._saldo -= valor 
        self.detalhes() 


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite 

    def sacar(self):
        if (self._saldo + self._limite) < valor:
            print('Saldo Insuficiente') 
            return 

        self._saldo -= valor 
        self.detalhes() 
    
    
    
    