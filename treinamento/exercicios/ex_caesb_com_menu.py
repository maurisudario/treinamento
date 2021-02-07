# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

print("Calculo conta CAESB")
consumo = float(input("Quantidade que foi consumida: "))
quantidade_de_unidades = int(input("Quantidade de unidade: "))
consumo_medio = (consumo / quantidade_de_unidades)
categoria = ''

while categoria != 1 or categoria != 2:
    categoria = int(input("Qual o tipo da categoria do imóvel ?\n[1] Residencial \n[2] Nao-residencial: "))
    if categoria == 1 or categoria == 2:
        break

if categoria == 1:
    tarifa_social = int(input("Possui direito a tarifa social?\n[1] Sim \n[2] Não "))
    if tarifa_social == '1':
        tarifa = 4.00
        if (consumo_medio <= 7):
            faixa = 1.49
        elif (consumo_medio >= 8 and consumo_medio <= 13):
            faixa = 1.79
        elif (consumo_medio >= 14 and consumo_medio <= 20):
            faixa = 3.55
        elif (consumo_medio >= 21 and consumo_medio <= 30):
            faixa = 5.33
        elif (consumo_medio >= 31 and consumo_medio <= 45):
            faixa = 17.05
        else:
            faixa = 23.87
    else:
        tarifa = 8.00
        if (consumo_medio <= 7):
            faixa = 2.99
        elif (consumo_medio >= 8 and consumo_medio <= 13):
            faixa = 3.59
        elif (consumo_medio >= 14 and consumo_medio <= 20):
            faixa = 7.10
        elif (consumo_medio >= 21 and consumo_medio <= 30):
            faixa = 10.66
        elif (consumo_medio >= 31 and consumo_medio <= 45):
            faixa = 17.05
        else:
            faixa = 23.87
else:
    tarifa = 21.00
    if (consumo_medio <= 4):
        faixa = 6.14
    elif (consumo_medio >= 5 and consumo_medio <= 7):
        faixa = 7.68
    elif (consumo_medio >= 8 and consumo_medio <= 10):
        faixa = 9.98
    elif (consumo_medio >= 11 and consumo_medio <= 40):
        faixa = 12.48
    else:
        faixa = 14.97

print ("")
print ("Cada residencia consumiu em média: {:.2f}".format(consumo_medio),'m³', '\n')

print("Alíquota Preço p/ m³: {:.2f}".format(faixa),'\n')

valor_gasto = (consumo_medio * faixa * quantidade_de_unidades ) + (tarifa * quantidade_de_unidades)

print ("Valor total do consumo de todas as unidades + tarifa fixa: R$ {:.2f}".format(valor_gasto),'\n')

conta_agua = (valor_gasto / quantidade_de_unidades)

print ("Valor do consumo da conta de água + tarifa fixa (cada residência): R$ {:.2f}".format(conta_agua),'\n')

condicao_do_imovel = str(input("O imóvel está em obra ?\n[1] Sim \n[2] Não "))


if (condicao_do_imovel == 1):
    total_a_pagar = conta_agua * 1.5
    print ("")
    print ("Conta total incluindo (Água + Esgoto + Taxas) R$ {:.2f}".format(total_a_pagar))
else:
    tipo_do_imovel = int(input("Qual o tipo de sistema ?\n[1] Convencional \n[2] Condominial "))
    if (tipo_do_imovel == 1):
        print ("")
        total_a_pagar = conta_agua * 2
        print ("Conta total incluindo (Água + Esgoto + Taxas) R$ {:.2f}".format(total_a_pagar))
    else:
        print("")
        total_a_pagar = conta_agua * 1.6
        print ("Conta total incluindo (Água + Esgoto + Taxas) R$ {:.2f}".format(total_a_pagar))
