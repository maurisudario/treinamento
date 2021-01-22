medida = float(input('Digite quantos metros quadrados deseja pintar: '))
litros = medida / 6
latas = litros // 18 +1
galoes = litros // 3.6 +1
preco_latas = latas * 80
preco_galoes = galoes * 25
combinacao = (litros//18)*80+((litros%18)//3.6+1)*25
print ('O preço so com latas é: ', preco_latas)
print ('O preço so com galões é: ', preco_galoes)
print ('O preço com a combinação é: ', combinacao)