# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

print("Calculo conta CAESB")
consumo = float(input("Quantidade que foi consumida: "))
quantidade_de_unidades = int(input("Quantidade de unidade: "))
consumo_medio = (consumo / quantidade_de_unidades)
categoria = ''

while categoria != 'residencial' or categoria != 'nao-residencial':
    categoria = str(input("A categoria da unidade é residencial ou nao-residencial? ")).lower()
    if categoria == 'residencial' or categoria == 'nao-residencial':
        break



if categoria == 'residencial':
    tarifa_social = str(input("Possui direito a tarifa social? (sim ou não) ")).lower()
    if tarifa_social == 'sim':
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

condicao_do_imovel = str(input("O imóvel está em obra ? ")).lower()


if (condicao_do_imovel == "sim"):
    total_a_pagar = conta_agua * 1.5
    print ("")
    print ("Conta total incluindo (Água + Esgoto + Taxas) R$ {:.2f}".format(total_a_pagar))
else:
    tipo_do_imovel = str(input("Qual o tipo de sistema: convencional ou condominial ?")).lower()
    if (tipo_do_imovel == 'convencional'):
        print ("")
        total_a_pagar = conta_agua * 2
        print ("Conta total incluindo (Água + Esgoto + Taxas) R$ {:.2f}".format(total_a_pagar))
    else:
        print("")
        total_a_pagar = conta_agua * 1.6
        print ("Conta total incluindo (Água + Esgoto + Taxas) R$ {:.2f}".format(total_a_pagar))

