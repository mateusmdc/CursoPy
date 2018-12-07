from cachorro import Cachorro
from gato import Gato
from time import sleep

nome = str(input('Digite o nome: '))
idade = int(input('digite a idade: '))
patas = int(input('Digite o numero de patas: '))
animal1 = Cachorro(nome, idade, patas)



print('Nome do animal: {}'.format(animal1.nome))

for c in range(1,10):
	print('...',end='', flush=True)
	sleep(1)

animal1.latir()

variavel = animal1.TrazQntsSapatos()

print(variavel)
