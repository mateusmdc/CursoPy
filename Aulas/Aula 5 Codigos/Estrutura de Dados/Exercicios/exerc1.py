expressao = str(input('digite a expressao: '))

exprespilha = []

for c in expressao:
	if c == '(':
		exprespilha.append('(')
	elif c == ')':
		if len(exprespilha) == 0:
			exprespilha.append(')')			
			break
		else:
			exprespilha.pop()

if len(exprespilha) == 0:
	print('expressao valida: ')

else:
	print('expressao invalida')


