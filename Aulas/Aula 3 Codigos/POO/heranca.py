class A:
	def __init__(self):
		self.__a = 'a'
		self.b = 'b'

class B(A):
	def __init__(self):
		self.c = 'c'
		super().__init__()

b = B()
if(isinstance(b, B)):
	print('b é B')

if(isinstance(b, A)):
	print('b é A')
