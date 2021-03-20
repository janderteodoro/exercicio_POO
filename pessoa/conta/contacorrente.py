from contas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, value):
        if not isinstance(value, (int, float)):
            print('Valor para saque em Conta Corrente precisa ser numérico')
            return

        if (self.saldo + self.limite) < value:
            print('Saldo Insuficiente')
            return

        self.saldo -= value
        self.detalhes()
