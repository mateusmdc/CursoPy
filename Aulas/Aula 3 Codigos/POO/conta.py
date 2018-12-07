class Conta():
	def __init__(self, Titular, CPFTitular):		
		self.Titular = Titular
		self.CPFTitular = CPFTitular
		self.__Saldo = 0.0


	def get_Saldo(self):
		return self.__Saldo

	def set_Saldo(self, novo)
		self.__saldo = novo

	def Sacar(self, saque):
		if (self.__Saldo >= saque):
			self.__Saldo -= saque
			print('novo saldo: {}'.format(self.__Saldo))
		else:
			print('saldo indisponivel')

	def Depositar(self, deposito):

		self.__Saldo += deposito
		print('novo saldo: {}'.format(self.__Saldo))

class ContaCorrente(Conta):
	def __init__(self, nome, cpf):
		super.__init(nome, cpf)

class ContaPoupanca(Conta):
	def __init__(self, nome, cpf)
	super.__init(nome, cpf)
	def render(self):
		novo = self.Saldo + (self.Saldo + self.rendimento)
		self.set_Saldo(novo)

class ContaConjunta(Conta):
	def __init__(self, nome, cpf):
		super.__init(nome, cpf)

c= ContaConjunta(('José', 'Maria'), ('02932', '139714')
