vh = float(input('Valor da hora trabalhada:'))
qh = int(input('Quantidade de horas trabalhadas:'))

salb = vh * qh
inss = 8/100 * salb
sind = 5/100 * salb
ir = 11/100 * salb

sall = salb - inss - sind - ir

print (' + Salário Bruto: R$ %.2f' %salb)
print (' - IR: R$ %.2f' %ir)
print (' - INSS: R$ %.2f' %inss)
print (' - Sindicato: R$ %.2f' %sind)
print (' = Salário Liquido: R$ %.2f' %sall)