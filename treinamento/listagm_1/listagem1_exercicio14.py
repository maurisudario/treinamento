peso = float(input('Digite o peso do peixe em Kg:'))
if peso > 50:
    excedente = peso - 50
    multa = excedente * 4
else:
    excedente = 0
    multa = 0
print ('Peso do peixe: %.2f Kg' %peso)
print ('Excesso em Kg: %.2f Kg' %excedente)
print ('Multa por exedente: R$ %.2f' %multa)