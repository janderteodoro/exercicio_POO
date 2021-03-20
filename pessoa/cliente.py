from pessoa.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.contas = []

    def adicioar_conta(self, conta):
        self.contas.append(conta)

    def detalhes_cliente(self):
        quantidade = len(self.contas)
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nQuantidade de Contas: {quantidade}')
        print()
        for conta in self.contas:
            conta.detalhes()


