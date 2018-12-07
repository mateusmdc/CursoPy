from cliente import Cliente
from enfermeiro import Enfermeiro
from medico import Medico
from time import sleep

nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso em kilogramas: '))
altura = float(input('Digite sua altura em metros: '))
idade = int(input('Digite sua idade: '))

cliente1 = Cliente(nome, peso, altura, idade)

enfermeiro1 = Enfermeiro()
enfermeiro1.calculoIMC(cliente1)

medico1 = Medico()

for c in range(1,6):
	print('...\n',end='', flush=True)
	sleep(1)

medico1.validaIMC(enfermeiro1, cliente1)

cliente1.ciente()

