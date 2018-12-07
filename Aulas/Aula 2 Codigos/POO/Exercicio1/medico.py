class Médico():
	def validaIMC(imc):
		if 16 <= imc <= 16.2:
			print("Muito abaixo do peso. O que pode acontecer: Queda de cabelo, infertilidade, ausência menstrual")
		elif 17 <= imc <= 18.4:
			print("Abaixo do peso. O que pode acontecer: Fadiga, stress, ansiedade")
		elif 18.5 <= imc <= 24.9:
			print("Peso Normal. Menor risco de doenças cardíacas e vasculares")
		elif 25 <= imc <= 29.9:
			print("Acima do peso. O que pode acontecer: Fadiga, má circulação, varizes")
		elif 30 <= imc <= 34.9:
			print("Obesidade Grau 1. O que pode acontecer: Diabetes, angina, infarto, aterosclerose")
		elif 35 <= imc <= 40:
			print("Obesidade Grau 2. O que pode acontecer: Apneia do sono, falta de ar")
		elif imc > 40:
			print("Obesidade Grau 3. O que pode acontecer: Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC")
