from banco import Banco
from cliente import Cliente
from contas import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Jander', 22)
cliente2 = Cliente('Thayssa', 22)
cliente3 = Cliente('Geraldo', 55)

conta1 = ContaCorrente(0000, 28334)
conta2 = ContaPoupanca(9999, 28192)
conta3 = ContaPoupanca(8888, 28374)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)


banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(141)
else:
    print('Cliente não autenticado')




