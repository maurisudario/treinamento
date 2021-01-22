tamanho = float(input('Digite o tamanho do arquivo em MB '))
velocidade = float(input('Digite a velocidade de Internet em MBp/s: '))
print('O tempo aproximado de download é de: %.0f minutos ' %((tamanho / velocidade) * 60))