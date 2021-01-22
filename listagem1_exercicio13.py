sx = int(input('Escolha: 1 para sexo Masculino / 2 para sexo Feminino: '))
h = float(input('Digite sua altura em metros:'))

if sx == 1:
    print ('Peso ideal será: ', (72.7*h) - 58)
else:
    print('Peso ideal será: ', (62.1*h) - 44.7)