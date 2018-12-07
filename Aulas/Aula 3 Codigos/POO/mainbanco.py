from conta import Conta

Titular = str(input('Digite o nome do Titular: '))
CPFTitular = str(input('Digite o CPF: '))

conta1 = Conta(Titular, CPFTitular)

deposito = float(input('Digite a quantidade que deseja depositar: '))
conta1.Depositar(deposito)
saque = float(input('Digite a quantidade que deseja sacar: '))
conta1.Sacar(saque)
