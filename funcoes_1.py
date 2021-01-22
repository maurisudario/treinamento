# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

def ex01():
    """ Faça um programa para imprimir:
     1
     2   2
     3   3   3
     .....
     n   n   n   n   n   n  ... n
     para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até
     a n-ésima linha. """

    def exercicio_1(n):
        for i in range(n):
            i += 1
            print(str(i) * i)

    n = int(input('Digite um número: '))
    exercicio_1(n)


def ex02():
    """ Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha. """

    def imprimir(valor):
        if isinstance(valor, int):
            x = 1
            while x <= valor:
                y = 1
                texto = ''
                while y <= x:
                    texto += str(y) + "\t"
                    y += 1
                print
                texto
                x += 1

def ex03():
    """ Faça um programa, com uma função que necessite de três argumentos, e que forneça a
    soma desses três argumentos. """

    def soma(numero1, numero2, numero3):
        soma = (numero1 + numero2 + numero3)

        return soma


    numero1 = int(input("Digite o Primeiro Número: "))

    numero2 = int(input("Digite o Segundo Número: "))

    numero3 = int(input("Digite o Terceiro Número: "))

    soma = soma(numero1, numero2, numero3)

    print("a soma é", soma)

def ex04():
    """ Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
    caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo. """

    def pn(n):
        if n > 0:
            print('Positivo')
        elif n == 0:
            print('Nulo')
        else:
            print('Negativo')

    print('POSITIVO OU NEGATIVO')
    n = int(input('digite um número: '))
    print('Este número é', end=' ')
    pn(n)

def ex05():
    """ Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais:
    taxa_imposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo
    de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. """

    def somaImposto(taxaImposto, Custo):
        return (1 + taxaImposto / 100) * Custo

    t = float(input('Digite a taxa de imposto: '))
    c = float(input('Digite o custo: '))
    print('Valor com imposto:', somaImposto(t, c))

def ex06():
    """ Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
    o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos
    duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um
    valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal
    para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos
    valores de entrada todas as vezes que desejar. """

    def converta(h, m):
        if 0 < h <= 12 and 0 < m < 60:
            print(f'{h}:{m} AM')
        elif 12 < h < 24 and 0 < m < 60:
            print(f'{h - 12}:{m} PM')
        else:
            print('Valor inválido')

    while True:
        h = int(input('Hora: '))
        if h == 999: break
        m = int(input('Minuto: '))
        converta(h, m)
        print('=' * 12

def ex07():
    """ Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação
    de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e
    passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor
    ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o
    programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor
    igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
    que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito
    da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3%
    de multa, mais 0,1% de juros por dia de atraso. """

    def valorPagamento(p, d):
        return p * 1.03 + 0.001 * d

    c = t = 0

    while True:
        p = float(input('Valor da prestação: '))
        if p == 0:
            print(f'Total: {t}. Quantidade: {c} ')
            break
        d = int(input('Dia em atraso: '))
        print(f'Valor a ser pago: {valorPagamento(p, d) :.2f}')
        print('-+-' * 10)
        c += 1
        t += valorPagamento(p, d)

def ex08():
    """Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.  """

    def inteiros(n):
        return len((str(n)))

    n = str(input('Digite um número: ')).strip()
    print(f'Esse número tem {inteiros(n)} dígitos')

def ex09():
    """ Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
    Por exemplo: 127 -> 721. """

    def reverso(n):
        return str(n[::-1])

    n = str(input('Digite um número: ')).strip()
    print(f'Reverso: {reverso(n)}')

def ex10():
    """Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
    obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
    Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada,
    você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar
    este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.  """

    import random
    def lancar_dados():
        return random.randint(2, 12)

    entrada = ""
    jogada = 0
    ponto = 0
    print
    "digite  \"sair\" para sair (sem aspas)\naperte <enter> para rolar os dados: "

    while (entrada != "sair"):
        jogada += 1
        print
        "Jogada {}".format(jogada)
        entrada = raw_input("Esperando acao: ")

        if entrada == "sair":
            print
            "Saindo do jogo... Tchau"
        else:
            if jogada > 1:
                print
                "Seu ponto e {}".format(ponto)
            valor = lancar_dados()
            print
            "O valor do dado e {}\n\n".format(valor)
            if jogada == 1:
                if valor == 7 or valor == 11:
                    print
                    "Voce tirou um natural e ganhou, PARABENS"
                    exit()
                elif valor == 2 or valor == 3 or valor == 12:
                    print
                    "Voce tirou um craps e perdeu, melhor sorte da proxima vez"
                    exit()
                else:
                    ponto = valor
            else:
                if valor == 7:
                    print
                    "Voce tirou um 7 antes de repetir seu ponto, voce perdeu"
                    exit()
                elif ponto == valor:
                    print
                    "Voce conseguiu repetir seu ponto e ganhou, Parabens"
                    exit()

def ex11():
    """ Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma
    string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja
    inválida. """

    def validaData(data):
        global m, d, a
        data = data.split('/')
        m = data[1]
        m = int(m)
        d = data[0]
        d = int(d)
        a = data[2]
        a = int(a)
        if m > 0 or m < 13:
            if m == 2:
                if d == 29:
                if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):  # ano bissexto
                return "VALIDA"
        else:
            return "NULL"
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d > 0 and d <= 31:  # mês de 31 dias
            return "VALIDA"
        else:
            return "NULL"
        elif m == 4 or m == 6 or m == 9 or m == 11:
        if d > 0 and d <= 30:  # mês de 30 dias
            return "VALIDA"
        else:
            return "NULL"
        else:
        return ("NULL")

    print("***** Data com mês por extenso. *****")
    data = input("Digite uma data com o seguinte formato dd/mm/aaaa: ")
    mes = ['
           ','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','
           Novembro','Dezembro']
           valida = validaData(data)
    if valida == "VALIDA":
        print("Data com mês por extenso: ", str(d), "de", str(mes[m]), "de", str(a))
    else:
        print("Data inválida!")

def ex12():
    """ Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string
    com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo,
    ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os
    caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados. """

    from random import shuffle
    def embaralha(nome):
        a = list(nome)
        shuffle(a)
        a = ''.join(a)
        print(a.lower())

    nome = input('Digite algo: ')
    embaralha(nome)

def ex13():
    """Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
    Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo
    igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para
    valores dentro da faixa de forma elegante.  """

    def ret(l, a):
        if l > 20:
            l = 20
        if a > 20:
            a = 20
        print('-+-' * l)
        c = 0
        while c < a:
            z = '|'
            print(f'{z}{z:>{(l * 3 - 1)}}')
            c += 1
        print('-+-' * l)

    l = int(input('Digite a largura: '))
    a = int(input('Digite a altura: '))
    ret(l, a)

def ex14():
    """Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição
    e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3,
    com números de 1 a 9:
    8  3  4
    1  5  9
    6  7  2
    Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
    Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
    Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.  """

    
