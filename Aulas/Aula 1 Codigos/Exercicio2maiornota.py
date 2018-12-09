x = float(input('Digite a primeira nota: '))
y = float(input('Digite a segunda nota: '))
z = float(input('Digite a terceira nota: '))

if (x > y) and (x > z):
    print('A primeira nota foi a maior')
          
elif (y > z) and (y > x):
    print('A segunda nota foi a maior')

elif (z > x) and (z > y):
    ('A terceira nota foi a maior')

else:
    print('nenhuma das notas foi a maior')
