class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        if not isinstance(value, (int, float)):
            print('Valor para a idade precisa ser numérico')
            return

        self._idade = value

