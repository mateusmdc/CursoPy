try:
	a = int(input())
	b = int(input())
	c = (a / b)
except ValueError as e:
	print('deu erro')
	raise e
except ZeroDivisionError:
	print('impossivel dividir por zero')
else:
	print(c)
finally:
	print('fim')
