class Banco:
    def __init__(self, nome):
        self.contas_registradas = []
        self.nome = nome
        self.agencia = 123

    def adicionar_cliente(self, cliente):
        for conta in cliente.contas:
            if conta.agencia == self.agencia:
                self.contas_registradas.append(cliente)
            else:
                print('Agência não corresponde à este banco')
                return

    def listar_clientes(self):
        for cliente in self.contas_registradas:
            print(f'Nome: {cliente.nome}')
            print(f'Idade: {cliente.idade}')
            for c in cliente.contas:
                c.detalhes()








