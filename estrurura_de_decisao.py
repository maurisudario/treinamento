# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'


def ex01():
    """  Faça um Programa que peça dois números e imprima o maior deles."""

    n1 = input('Digite o primero numero: ')
    n2 = input('Digite o segundo numero: ')

    if n1 > n2:
        print(n1, 'é maior que', n2)
    elif n2 > n1:
        print(n2, 'é maior que', n1)
    else:
        print('os numeros são iguais')

def ex02():
    """ Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. """

    n = int(input("Aqui vai o valor que o usuário irá digitar:"))

    if (n < 0):

    print("O valor digitado é negativo!")

    else:

    print("O valor digitado é positivo!")

def ex03():
    """ Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
    F - Feminino, M - Masculino, Sexo Inválido. """

    sexo = str(input('Digite (F)-Feminino, (M)-Masculino: ').upper())
    if sexo == 'M':
        print('Sexo Masculino.')
    elif sexo == 'F':
        print('Sexo Feminino.')
    else:
        print('Sexo Inválido.')

def ex04():
    """ Faça um Programa que verifique se uma letra digitada é vogal ou consoante. """


    letra = input("Digite uma letra: ")
    vogais = ['a', 'e', 'i', 'o', 'u']

    if letra in vogais:
        print('VOGAL')
    else:
        print('CONSOANTE')

def ex05():
    """ Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
    calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez."""

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 7 and media < 10:
        print("APROVADO")
    elif media < 7:
        print("REPROVADO")
    else:
        print("APROVADO com DISTINÇÃO")

def ex06():
    """Faça um Programa que leia três números e mostre o maior deles.  """

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    valores = [valor1, valor2, valor3]

    print(f'O maior número é {max(valores)}')

def ex07():
    """ Faça um Programa que leia três números e mostre o maior e o menor deles. """

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    lista = [valor1, valor2, valor3]

    print("Menor valor: ", min(lista), "\nMenor valor: ", max(lista))

def ex08():
    """ Faça um programa que pergunte o preço de três produtos e informe qual produto
    você deve comprar, sabendo que a decisão é sempre pelo mais barato. """

    preco1 = float(input("Digite o primeiro preço: "))
    preco2 = float(input("Digite o segundo preço: "))
    preco3 = float(input("Digite o terceiro preço: "))

    lista = [preco1, preco2, preco3]

    print("O produto que deve ser comprado é o que custa ", min(lista))



def ex09():
    """  Faça um Programa que leia três números e mostre-os em ordem decrescente."""

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    lista = [n1, n2, n3]

    lista.sort(key=float, reverse=True)

    print("decrescente: ", lista)

def ex10():
    """ Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino
    ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
    ou "Valor Inválido!", conforme o caso. """

    horario = input("Digite [M, V, N]: ").upper()

    if horario == 'M':
        print("Bom Dia")
    elif horario == 'V':
        print("Boa Tarde")
    elif horario == 'N':
        print("Boa Noite")
    else:
        print("Valor Inválido")

def ex11():
    """ As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
    contrataram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
    baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. """

    salario = float(input("Digite o seu salário"))

    valor_baixo = salario * 0.20
    baixo = salario * 1.20
    valor_medio = salario * 0.15
    medio = salario * 1.15
    valor_alto = salario * 0.10
    alto = salario * 1.10
    valor_altissimo = salario * 0.05
    altissimo = salario * 1.05

    print("Antes Reajuste: ", salario)

    if salario <= 280:
        print("Aumento: 20%\nValor: ", valor_baixo, "\nFinal: ", baixo)
    elif salario > 200 and salario <= 700:
        print("Aumento: 15%\nValor: ", valor_medio, "\nFinal: ", medio)
    elif salario > 700 and salario <= 1500:
        print("Aumento: 10%\nValor: ", valor_alto, "\nFinal: ", alto)
    else:
        print("Aumento: 5%\nValor: ", valor_altissimo, "\nFinal: ", altissimo)

def ex12():
    """ Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
    Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o
    FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
    O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
    o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme
    o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00 """

    valor_hora = float(input("Quanto você ganha por hora? "))
    horas_mes = int(input("Quantas horas você trabalha no mês? "))
    salario_bruto = horas_mes * valor_hora

    ir1500 = salario_bruto * 0.05
    ir2500 = salario_bruto * 0.10
    irmaior = salario_bruto * 0.20

    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11

    print("salario Bruto: ", salario_bruto)

    if salario_bruto <= 900:
        print("Seu salario permanecerá o mesmo")
    else:
        print("INSS: ", inss, "\nFGTS: ", fgts)

    if salario_bruto > 900 and salario_bruto <= 1500:
        salario_liquido = float(salario_bruto) - float(ir1500) - float(inss)
        print("IR: ", ir1500, "\nSalario Liquido: ", salario_liquido)

    elif salario_bruto > 1500 and salario_bruto <= 2500:
        salario_liquido = float(salario_bruto) - float(ir2500) - float(inss)
        print("IR: ", ir2500, "\nSalario Liquido: ", salario_liquido)

    else:
        salario_liquido = float(salario_bruto) - float(irmaior) - float(inss)
        print("IR: ", iralto, "\nSalario Liquido: ", salario_liquido)

def ex13():
    """ Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
    se digitar outro valor deve aparecer valor inválido. """

    dia = int(input("Digite um número de 1 a 7: "))

    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    elif dia == 7:
        print("Sababo")
    else:
        print("Valor Inválido")

def ex14():
    """ Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um
    semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0        A
    Entre 7.5 e 9.0         B
    Entre 6.0 e 7.5         C
    Entre 4.0 e 6.0         D
    Entre 4.0 e zero        E
   O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
   se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. """

    nota1 = float(input("Digite a nota1"))
    nota2 = float(input("Digite a nota2"))
    media = (nota1 + nota2) / 2

    if media >= 0 and media <= 4:
        print("E")
    elif media > 4 and media <= 6:
        print("D")
    elif media > 6 and media <= 7.5:
        print("C")
    elif media > 7.5 and media <= 9:
        print("B")
    else:
        print("A")

def ex15():
    """ Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
    ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; """

    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))

    if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
        print("É UM TRINGULO")
        if lado1 == lado2 and lado1 == lado3:
            print("Equilatero")
        elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
            print("Isóceles")
        else:
            print("Escaleno")
    else:
        print("Não é um TRINGULO")

def ex16():
    """ Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
    O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
    nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve
    fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; """


    import math

    a = float(input("Digite A: "))
    if a == 0:
        print("Valor Invalido")
    else:
        b = float(input("Digite B: "))
        c = float(input("Digite C: "))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("A equação não possui raizes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
    if delta == 0:
        print("1 Raiz real: ", x1)
    else:
        print("2 raizes reais, x1: ", x1, "\nx2: ", x2)

def ex17():
    """ Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe
    se este ano é ou não bissexto. """

    ano = int(input("Digite o ano"))

    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print("Bissexto")
    else:
        print("Não Bissexto")

def ex18():
    """ Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. """

    data = input("Digite a data no seguinte modelo: [11/07/2002] :")
    if len(data) != 10:
        print("ERRADO")
    else:
        if data[2] != '/' or data[5] != '/':
            print("ERRADO")
        else:
            numeros_data = data.split('/')
            if int(numeros_data[0]) > 31:
                print("ERRADO")
            elif int(numeros_data[1]) > 12:
                print("ERRADO")
            else:
                print("CERTO")

def ex19():
    """ Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de
    centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111,
    25, 20, 10, 21, 11, 1, 7 e 16 """

    import math
    numero = int(input("Digite um número menor ou igual a 1000: "))
    if numero <= 1000:
        centena = numero / 100
        centena2 = math.floor(float(centena))
        resto_centena = centena - centena2
        resto_multiplicado = resto_centena * 100

        dezena = resto_multiplicado / 10
        dezena2 = math.floor(float(dezena))
        unidade = dezena - dezena2
        unidade_certo = unidade * 10

        print("Centena(s): ", centena2)
        print("dezena(s): ", dezena2)
        print("Unidade(s): ", round(unidade_certo))

    else:
        print("VOCÊ DIGITOU UM NÚMERO MAIOR QUE 1000")

def ex20():
    """ Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular
    a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. """

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 7 and media < 10:
        print("APROVADO")
    elif media < 7:
        print("REPROVADO")
    else:
        print("APROVADO com DISTINÇÃO")

def ex21():
    """ Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do
    saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão
    as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa
    não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
    uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
    uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. """

    import math
    saque = int(input("Valor para sacar: "))
    nota100 = saque / 100
    nota100_certo = math.floor(nota100)
    resto_nota_100 = (nota100 - nota100_certo) * 100

    nota50 = resto_nota_100 / 50
    nota50_certo = math.floor(nota50)
    resto_nota_50 = (nota50 - nota50_certo) * 50

    nota10 = resto_nota_50 / 10
    nota10_certo = math.floor(nota10)
    resto_nota_10 = (nota10 - nota10_certo) * 10

    nota5 = resto_nota_10 / 5
    nota5_certo = math.floor(nota5)
    nota1 = (nota5 - nota5_certo) * 5

    print("Notas 100: ", nota100_certo, "\nNotas50: ", nota50_certo, "\nNota 10: ", nota10_certo, "\nNota 1: ",
          round(nota1))

def ex22():
    """ Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica:
    utilize o operador módulo (resto da divisão). """

    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número Impar")

def ex23():
    """ Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
    Dica: utilize uma função de arredondamento. """

    numero = float(input("Digite um número: "))

    if (numero // 1 == numero):
        print("numero inteiro")
    else:
        print("Numero Decimal")

def ex24():
    """ Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação
    ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. """

    numero1 = float(input("Digite o número 1: "))
    numero2 = float(input("Digite o número 2: "))
    operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")

    def checar():
        if (resultado_operacao // 1 == resultado_operacao):
            print("Inteiro")
            if resultado_operacao % 2 == 0:
                print("Par")
                if resultado_operacao > 0:
                    print("Positivo")
                else:
                    print("Negativo")
            else:
                print("Impar")
        else:
            print("Decimal")

    if operacao == '+':
        resultado_operacao = numero1 + numero2
        print("Resultado: ", resultado_operacao)
        checar()
    elif operacao == '-':
        resultado_operacao = numero1 - numero2
        print("Resultado: ", resultado_operacao)
        checar()
    elif operacao == '/':
        resultado_operacao = numero1 / numero2
        print("Resultado: ", resultado_operacao)
        checar()
    elif operacao == '*':
        resultado_operacao = numero1 * numero2
        print("Resultado: ", resultado_operacao)
        checar()
    else:
        print("Valor Invalido")

def ex25():
    """ Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
    participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
    classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
    ele será classificado como "Inocente". """

    perguntas = [
        "Telefonou para a vítima?: ",
        "Esteve no local do crime?: ",
        "Mora perto da vítima?: ",
        "Devia para a vítima?: ",
        "Já trabalhou com a vítima?: "
    ]
    resposta = 0

    for status in perguntas:
        resposta += (input(status) == "sim")

    if resposta == 5:
        print("Assassino")

    elif resposta >= 3:
        print("Cúmplice")

    elif resposta == 2:
        print("Suspeito")

    else:
        print("Inocente")

def ex26():
    """ Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
    o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor
    a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool
    é R$ 1,90. """

    litros = int(input("Digite a quantidade de litros: "))
    combustivel = input("Digite o tipo do combustivel [G, A]: ")

    preco_alcool1 = (1.90 * 0.03)
    preco_alcool2 = (1.90 * 0.05)
    preco_gasolina1 = (2.50 * 0.04)
    preco_gasolina2 = (2.50 * 0.06)

    print("Litros Vendidos: ", litros)

    if combustivel == 'a' or combustivel == 'A':
        print("Combustivel: alcool")
        if litros <= 20:
            desconto = (1.90 - preco_alcool1) * litros
            print("Preço: ", desconto)
        else:
            desconto = (1.90 - preco_alcool2) * litros
            print("Preço: ", desconto)
    elif combustivel == 'g' or combustivel == 'G':
        print("Combustivel: gasolina")
        if litros <= 20:
            desconto = (2.50 - preco_gasolina1) * litros
            print("Preço: ", desconto)
        else:
            desconto = (2.50 - preco_gasolina2) * litros
            print("Preço: ", desconto)
    else:
        print("Valor Invalido")

def ex27():
    """ Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                Até 5 Kg                             Acima de 5 Kg
    Morango  R$ 2,50 por Kg                         R$ 2,20 por Kg
    Maçã    R$ 1,80 por Kg                          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
    de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. """

    morangos = int(input("Digite a quantidade de morangos [kg]: "))
    macas = int(input("Digite a quantidade de maças [kg]: "))
    preco_morango1 = morangos * 2.50
    preco_morango2 = morangos * 2.20

    preco_maca1 = macas * 1.80
    preco_maca2 = macas * 1.50

    print("quantidade de maçãs: ", macas, "\nQuantidade de morangos: ", morangos)

    if morangos > 5:
        preco_certo_morango = preco_morango1
    else:
        preco_certo_morango = preco_morango2

    if macas > 5:
        preco_certo_maca = preco_maca1
    else:
        preco_certo_maca = preco_maca2

    preco_total = preco_certo_maca + preco_certo_morango

    if preco_total > 25 or (macas + morangos) > 8:
        print("Preço final: ", (preco_total - (preco_total * 0.1)))
    else:
        print("Preço final: ", preco_total)

def ex28():
    """ O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg                        Acima de 5 Kg
    File Duplo        R$ 4,90 por Kg                      R$ 5,80 por Kg
    Alcatra           R$ 5,90 por Kg                      R$ 6,80 por Kg
    Picanha           R$ 6,90 por Kg                      R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
    cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a
    quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
    tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. """

    tipo_carne = input("Digite o tipo da carne que irá comprar: ")
    quantidade_carne = int(input("Digite a quantidade de carne que irá comprar: "))
    tipo_pagamento = input("Escreva o tipo de tipo de pagamento: ")

    print("Tipo de carne:", tipo_carne, "\nQuantidade de carne:", quantidade_carne)

    preco_file_duplo1 = quantidade_carne * 4.90
    preco_file_duplo2 = quantidade_carne * 5.80

    alcatra1 = quantidade_carne * 5.90
    alcatra2 = quantidade_carne * 6.80

    picanha1 = quantidade_carne * 6.90
    picanha2 = quantidade_carne * 7.80

    if tipo_carne == 'filé duplo':
        if quantidade_carne > 5:
            preco_total = preco_file_duplo1
        else:
            preco_total = preco_file_duplo2
    elif tipo_carne == 'alcatra':
        if quantidade_carne > 5:
            preco_total = alcatra1
        else:
            preco_total = alcatra2
    elif tipo_carne == 'picanha':
        if quantidade_carne > 5:
            preco_total = picanha1
        else:
            preco_total = picanha2
    else:
        print("Carne Invalida")

    if tipo_pagamento == 'Cartão Tabajara':
        desconto = preco_total * 0.05
        print("Tipo de pagamento: ", tipo_pagamento)
        print("Valor do desconto: ", desconto)
        print("Valor Final: ", (preco_total - desconto))
    else:
        print("Tipo de pagamento: normal\nValor do desocnto: 0")
        print("Valor Final: ", preco_total)

