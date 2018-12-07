class Enfermeiro():
	def calculoIMC(self, cliente):
		imc = cliente.peso / (cliente.altura*cliente.altura)
		return imc
