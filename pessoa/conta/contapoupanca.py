from contas.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, value):
        if not isinstance(value, (int, float)):
            print('Valor para Saque em Conta Poupança precisa ser numérico')
            return

        if self.saldo < value:
            print('Saldo Insuficiente')
            return

        self.saldo -= value
        self.detalhes()
