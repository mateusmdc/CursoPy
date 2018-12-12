'''compras = ['Arroz', 'Feijão', 'Macarrão', 'Legumes']

almoco = compras[.]

compras.append('Carne')

print['Almoco']'''

'''print(sorted(compras))

for pos,item in enumerate(compras):
	print(f'{pos+1} - {item}.')'''


'''numeros = ('one', 'two', 'three')

(um, dois, tres) = numeros

print(um)'''

'''aluno = {'nome': 'Adrilene',
	'idade': 20, 
	'Semestre': 5}

print(aluno)

print(aluno.keys())
print(aluno.values())
print('')

for k,y in aluno.items():
	print(f'{k}: {y}.')'''

from random import randint
from time import sleep
from operator import itemgetter

aluno = {'Nome': 200, 'Idade': 20, 'Altura': 171}

#itemgetter(1)
atributos = sorted(aluno.items(), key=itemgetter(1), reverse = True)

print(atributos)


