'''jogador1 = {'nome':'kaka', 'posicao':'meio campo'}

jogador2 = {'nome':'ronaldo', 'posicao':'atacante'}

jogador3 = {'nome':'neuer', 'posicao':'goleiro'}

jogador4= {'nome':'marcelo', 'posicao': 'lateral'}'''

'''print(jogador.items())

print(jogador.keys())

print(jogador.values())'''


'''time = []
time.append(jogador1.copy())
time.append(jogador2.copy())
time.append(jogador3.copy())
time.append(jogador4.copy())

print(time)
print(time[1])'''

time = []
jogador = {}

for c in range(0,4):
	jogador['nome'] = str(input('digite o nome do jogador {}: '.format(c+1)))
	jogador['posicao'] = str(input('digite o posicao do jogador {}: '.format(c+1)))
	jogador['qtd gols'] = str(input('digite a qtd de gols do jogador {}: '.format(c+1)))

	time.append(jogador.copy())

print(time)
