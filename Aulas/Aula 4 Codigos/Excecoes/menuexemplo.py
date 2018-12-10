def menucaraio():
	

		
	print('Escolha uma das opções enumeradas:')
	print('1-opcaum\n2-opcaodois\n3-opcaotres\n')

	while(True):
		try:
			opcao = int(input())
		except ValueError:
			opcao = -1
			print('por favor digite apenas numeros')
		finally:
			if(opcao in (1, 2 ,3)):
				return opcao
			print('digite apenas uma das opcoes disponiveis')

menucaraio()
