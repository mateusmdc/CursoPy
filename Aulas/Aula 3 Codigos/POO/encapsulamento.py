class A:
	def __init__(self):
		self.__a = 'a'
		self.b = 'b'

	def get_a(self):
		return self.__a
	def set_a(self, novo):
		self.__a = novo

def main():
	a = A()
	print(a)

if(__name__ == '__main__'):
	main()
