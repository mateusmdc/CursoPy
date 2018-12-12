from random import randint
from time import sleep
from operator import itemgetter


jogo = {'Jogador1':randint(1,6),
	'Jogador2':randint(1,6),
	'Jogador3':randint(1,6),
	'Jogador4':randint(1,6) }


ranking = dict()

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

print('Resultado: ')

for k,v in jogo.items():
	print(f'{k} sorteou {y}.')
	sleep(1)

print('')
print('Ranking')
for pos,j in enumerate(ranking):
	print(f'{pos} - {j[0]}.')
	sleep(1)
