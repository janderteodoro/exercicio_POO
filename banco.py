from time import sleep


class Banco:
    def __init__(self):
        self.agencias = [0000, 9999, 8888]
        self.contas = []
        self.clientes = []

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def autenticar(self, cliente):
        print('Autenticando...')
        sleep(3)
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False

        print('Autenticado!!!')
        return True

