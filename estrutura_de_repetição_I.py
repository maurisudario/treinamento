# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

def ex01():
    """Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
    Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

numero = int(input("\n Digite um número: "))

if numero % 2 == 0 and numero != 2:
    print("não primo")
else:
    print("primo")

def ex02():
    """Copie e altere o programa de cálculo dos números primos, informando, caso o número não
     seja primo, por quais número ele é divisível."""

numero = int(input("\nDigite um número: "))
lista = []


if numero % 2 != 0 or numero == 2:
    print("primo")
else:
    for i in range(numero):
        if numero % (i + 1) == 0:

            lista.append(i + 1)

print("Os números divisiveis por ", numero, " são ", lista)

def ex03():
    """Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
     fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele
     executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o
      número de testes (divisões) executados."""

numero = int(input("\n Digite um número: "))
lista = []
divisoes = 0

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
        divisoes += 1
    else:
        divisoes += 1
print("Números primos: ", lista)
print("Número de divisões", divisoes)

def ex04():
    """Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles
    estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar
    quando for lido um número negativo."""

n25 = []
n50 = []
n75 = []
n100 = []
numero = True
while numero > 0:
    numero = float(input("Digite um número: "))
    if numero > 0 and numero <= 25:
        n25.append(numero)
    elif numero > 25 and numero <= 50:
        n50.append(numero)
    elif numero > 50 and numero <= 75:
        n75.append(numero)
    elif numero > 75 and numero <= 100:
        n100.append(numero)

print("\n[0, 25]: ", len(n25))
print("[26, 50]: ", len(n50))
print("[51, 75]: ", len(n75))
print("[76, 100]: ", len(n100))

def ex05():
    """Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a
    média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem,
    adulta ou idosa, conforme a média calculada."""

npessoas = int(input("Digite o número de pessoas que ira digitar a idade: "))
lista = []

for i in range(npessoas):
    idade = lista.append(int(input("Digite a idade: ")))


if sum(lista) / len(lista) < 25:
    print("jovem")
elif sum(lista) / len(lista) >= 25 and sum(lista) / len(lista) < 60:
    print("adulto")
else:
    print("idosa")

def ex06():
    """Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
     Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

eleitores = int(input("Digite o número de eleitores: "))
votos = []

for i in range(eleitores):
    voto = votos.append(int(input("Qual candidato deseja votar? [1, 2, 3]: ")))

print("Quantidade de votos para candidato 1: ", votos.count(1))
print("Quantidade de votos para candidato 2: ", votos.count(2))
print("Quantidade de votos para candidato 3: ", votos.count(3))

def ex07():
        """Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade
        de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

turmas = int(input("Quantas turmas? : "))
alunos_turmas = []
turma = 1

for i in range(turmas):
    print("turma ", turma)
    alunos = int(input("Alunos da turma : "))
    while alunos > 40:
        print("turma ", turma, " [uma turma só pode ter 40 alunos]")
        alunos = int(input("Alunos da turma : "))
    turma += 1
    alunos_turmas.append(alunos)

media = sum(alunos_turmas) / len(alunos_turmas)
print("A media e igual a: ", media)


def ex08():
    """Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o
     valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em
      cada um."""

quantCds = int(input("Digite a quantidade de CD's : "))
cds = []
ncd = 1

for i in range(quantCds):
    print("CD número ", ncd)
    valorCd = cds.append(float(input("Digite o valor do CD: ")))
    ncd += 1

media = sum(cds) / len(cds)
print("A media para cada CD é: ", media)


def ex09():
    """O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
    Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o
    número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa
    precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi
    contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços
    de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
..
50 - R$ 99.50."""

produtos = int(input("Digite a quantidade de produtos: "))
while produtos > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))


precos = []
nproduto = 1
count = 0

for i in range(produtos):
    print("Produto N° ", nproduto)
    preco = precos.append(float(input("Digite o preco do produto: ")))
    nproduto += 1

nproduto = 1
for j in range(produtos):
    print("Produto N° ", nproduto, "= ", precos[count])
    count += 1
    nproduto += 1


def ex10():
    """O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da
    tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa
    que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo
    usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
..
50 - R$ 9.00."""

paes = int(input("Digite a quantidade de pães: "))
while paes > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))

count = 1
precopao = float(input("Qual é o preço do pão? : "))

for j in range(paes):
    print(count, "= R$", round(precopao * count, 2))
    count += 1

def ex11():
    """ O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma
    loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
    O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
    Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então
    mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular
    e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para
    registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00"""

import time

while True:
    precosprodutos = []
    precoproduto = True
    nproduto = 1

    while precoproduto != 0:
        print("Produto n° ", nproduto)
        precoproduto = float(input("Digite o preço do produto: "))
        precos_produtos.append(precoproduto)
        nproduto += 1

    print("Total: ", sum(precosprodutos))
    dinheiro = float(input("Digite a quantida que irá pagar: "))

    while dinheiro < sum(precosprodutos):
        dinheiro = float(input("Digite a quantida que irá pagar[maior que o total da compra] : "))

    print("Dinheiro: R$", dinheiro)
    print("Troco: R$", dinheiro - sum(precosprodutos))
    print("\nPróxima compra em 3 segundos...")
    time.sleep(3)
    print("\n" * 5)

def ex12():
    """ Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
    Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um
    número inteiro e determine se ele é ou não um número primo."""


numero = int(input("\n Digite um número: "))

if numero % 2 == 0 and numero != 2:
    print("Número não primo")
else:
    print("Número primo")

print("A soma dos intervalos é: ", soma)

def ex13():
    """ Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos
     números primos existentes entre 1 e um número inteiro informado pelo usuário. """

numero = int(input("\n Digite um número: "))
lista = []

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

print("Números primos: ", lista)

def ex14():
    """ Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo
    usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final
    devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial. """

ntabuada = int(input("\n Digite o número para fazer a tabuada: "))
ninicial = int(input("Iniciar a tabuada no: "))
nfinal = int(input("Finalizar a tabuada no: "))

caminho = ninicial

for i in range(ninicial, nfinal + 1):
    print(ntabuada, " X ", caminho, " = ", ntabuada * caminho)
    caminho += 1

def ex15():
    """ Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o mais baixo,
    o mais pesado e o mais leve, para isto você deve fazer um programa que pergunte a cada um dos clientes
    da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário
    digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do
    cliente mais alto, do mais baixo, do mais pesado e do mais leve, além da média das alturas e dos pesos dos
    clientes. """

codclientes = []
alturaclientes = []
pesoclientes = []
ncliente = 1
codigo = True

while codigo != 0:
    print("\n Cliente n° ", n_cliente)
    codigo = int(input("Digite o código: "))
    if codigo == 0:
        break
    else:
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        codclientes.append(codigo)
        alturaclientes.append(altura)
        pesoclientes.append(peso)
        ncliente += 1

codmagro = pesoclientes.index(min(pesoclientes))
codgordo = pesoclientes.index(max(pesoclientes))
codalto = alturaclientes.index(max(alturaclientes))
codbaixo = alturaclientes.index(min(alturaclientes))
print("\n" * 5)
print("Código do mais magro: ", codclientes[cod_magro])
print("Código do mais gordo: ", codclientes[cod_gordo])
print("Código do mais alto: ", codclientes[cod_alto])
print("Código do mais baixo: ", codclientes[cod_baixo])
print("Média de altura: ", sum(alturaclientes) / len(alturaclientes))
print("Média de peso: ", sum(pesoclientes) / len(pesoclientes))

def ex16():
    """ Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
        Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
        Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
        A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano
        anterior. Faça um programa que determine o salário atual deste funcionário. """

salario = 1000
aumento = 1.5

for i in range(1996, 2018 + 1):
    aumento = aumento * 2
    salario_atual = salario + (salario * (aumento / 100))
    print("Salario em ", i, " = ", salario_atual)

def ex17():
    """ Em relação ao programa anterior, copie e altere para permitir que o usuário digite o salário inicial
        do funcionário. """

salario = float(input("Dgite o salario inicial do funcionario: "))
aumento = 1.5

for i in range(1996, 2018 + 1):
    aumento = aumento * 2
    salario_atual = salario + (salario * (aumento / 100))
    print("Salario em ", i, " = ", salario_atual)

def ex18():
    """ Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
        Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).


Deseja-se saber:
Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""

cod_cidades = []
n_veiculos = []
n_acidentes = []
acidentes_2000 = []

for i in range(5):
    print("\nCidade número ", i + 1)
    codigocidade = int(input("Digite o código da cidade: "))
    while codigocidade in codcidades:
        print("[Código já digitado]")
        codigocidade = int(input("Digite outro código: "))

    numeroacidentes = int(input("Digite o número de acidentes: "))
    numeroveiculos = int(input("Digite o número de veiculos: "))

    if numeroveiculos > 2000:
        acidentes2000.append(numeroacidentes)
        nacidentes.append(numeroacidentes)
    else:
        nacidentes.append(numeroacidentes)

    nveiculos.append(numeroveiculos)
    codcidades.append(codigocidade)

indiceacidentesmenor = nacidentes.index(min(nacidentes))
indiceacidentesmaior = nacidentes.index(max(nacidentes))

print("\nMenos acidentes\nQuantidade de acidentes: ", min(nacidentes), "\nCódigo da cidade: ", codcidades[indice_acidentesmenor])
print("\nMais acidentes\nQuantidade de acidentes: ", max(nacidentes), "\nCódigo da cidade: ", codcidades[indice_acidentesmaior])

mediaveiculos = sum(nveiculos) / len(nveiculos)
print("\nMédia de veiculos nas 5 cidades: ", mediaveiculos)

mediaacidentes2000 = sum(acidentes2000) / len(acidentes2000)
print("\nMédia de acidentes nas cidades com menos de 2000 veículos: ", mediaacidentes2000)

def ex19():
    """  Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
         valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
 Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67   """

print("\n" * 5)
divida = float(input("Digite o valor da divida: "))
parcela = 1
print("\n" * 5)
print("Valor da divida: ", end="  ")
print("Valor do juros: ", end="  ")
print("Quantidade de parcelas: ", end="  ")
print("Valor da parcela: ")

for i in range(5):
    if parcela == 1:
        juros = 1
        valor_juros = 0
    elif parcela == 4:
        parcela = 3
        juros = 1.10
    elif parcela == 7 or parcela == 6:
        parcela = 6
        juros = 1.15
    elif parcela == 10 or parcela == 9:
        parcela = 9
        juros = 1.20
    elif parcela == 13 or parcela == 12:
        parcela = 12
        juros = 1.25

    valorjuros = divida * (juros - 1)
    dividacomjuros = divida * juros
    valorparcela = dividacomjuros / parcela

    print("R$", round(dividacomjuros, 2), end="            ")
    print(round(valorjuros, 2), end="                  ")
    print(parcela, end="                        ")
    print("R$ ", round(valorparcela, 2))
    parcela += 3

def ex20():
    """  O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre
o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente
deve informar quando o pedido deve ser encerrado.   """


codigos = [100, 101, 102, 103, 104, 105]
comidas = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hamburguer', 'ChesseBurguer', 'Refrigerante']
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True
npedido = 1
pedido = []

while codigo != 0:
    print("\nPedido n°", npedido)
    codigo = int(input("Digite o código do alimento: "))
    if codigo == 0:
        break
    else:
        while codigo not in codigos:
            print("[Este código não corresponde a nenhum alimento.]")
            codigo = int(input("Digite o código do alimento: "))

        indice = codigos.index(codigo)
        quantidade = int(input("Digite a quantidade: "))
        valorpedido = precos[indice] * quantidade
        pedido.append(valorpedido)
    npedido += 1

pedidonota = 0
print("\n" * 2)
for i in range(npedido - 1):
    print("Pedido n°", pedidonota + 1, "= R$", round(pedido[pedidonota], 2))
    pedidonota += 1
print("Total: R$", round(sum(pedido), 2))

def ex21():
    """Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
       Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero. """

possiveisvotos = [1, 2, 3, 4, 5, 6]
candidatos = ['Ciro Gomes', 'Jair Bolsonaro', 'João Amoedo', 'Lula ', 'Nulo', 'Branco']
votos = []

voto = True
nvotos = 1
while voto != 0:
    print("Voto n°", nvotos)
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
    else:
        while voto not in possiveisvotos:
            print("[Voto invalido.]")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)
    nvotos += 1

contador = 0
print("\n" * 2)
for i in range(len(candidatos)):
    print("Votos para ", candidatos[contador], end=" : ")
    if votos.count == 0:
        print("0")
        contador += 1
    else:
        print(votos.count(contador + 1))
        contador += 1

porcentagemnulo = (votos.count(5) / len(votos)) * 100
porcentagembranco = (votos.count(6) / len(votos)) * 100
print("\nPorcentagem Nulos: ", round(porcentagemnulo, 2), "%\nPorcentagem Brancos: ", round(porcentagembranco, 2),"%")

def ex22():
    """Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa
    deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim
    calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o
    sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem
    respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito
da prova antes dos alunos usarem o programa. """

gabarito = []
respostasaluno = []
notastiradas = []
print("\nProfessor: ")
for i in range(10):
    print("Questão: ", i + 1)
    respostacerta = gabarito.append(input("Digite a alternativa correta: "))
naluno = 1
continuar = True
while continuar != 'n':
    print("\n" * 5)
    print("Aluno n°", naluno, ":")
    respostasaluno.clear()
    for i in range(10):
        print("Questão: ", i + 1)
        respostaaluno = respostasaluno.append(input("Escolha a alternativa: "))
    nota = 0
    for i in range(10):
        if respostasaluno[i] == gabarito[i]:
            nota += 1
    notastiradas.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ")
    naluno += 1
print(len(notastiradas), "alunos utilizaram o sistema")
print("\nA maior nota tirada foi: ", max(notastiradas))
print("A menor nota tirada foi: ", min(notastiradas))
print("A media de notas da turma foi de:", sum(notastiradas) / len(notastiradas))
print(notastiradas)

def ex23():
    """Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
    No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
    O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que
    receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a
    média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
    calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na
    ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for
    informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo: Atleta:

Rodrigo Curvêllo


Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m


Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m


Resultado final:
Rodrigo Curvêllo: 5.9 m """

nomeatleta = True
natleta = 1
while nomeatleta != '':
    saltos = []
    print("\n" * 5)
    print("Atleta n°", natleta)
    nomeatleta = input("Digite o nome do atleta: ")
    if nomeatleta == '':
        break
    else:
        nsalto = 1
        print("\n" * 3)
        for i in range(5):
            print("Salto n° ", nsalto)
            distanciasalto = float(input("Digite a distancia do salto: "))
            saltos.append(distanciasalto)
            n_salto += 1
        print("Atleta: ", nomeatleta)
        nsalto = 1
        count = 0
        for i in range(5):
            print(nsalto, "° salto : ", saltos[count]," m")
            nsalto += 1
            count += 1
        print("Melhor salto: ", max(saltos), " m")
        print("Pior salto: ", min(saltos), " m")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print("Media dos demais saltos: ", round(media, 2))
        print("Resultado Final: \n", nomeatleta, " : ", round(media, 2))
        natleta += 1

def ex24():
    """Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são
    eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o
    nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a
    sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média
    com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser
    conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7


Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04 """

import time
nomeatleta = True
natleta = 1
while nomeatleta != '':
    notas = []
    print("\n" * 5)
    print("Atleta n°", natleta)
    nomeatleta = input("Digite o nome do atleta: ")
    if nomeatleta == '':
        break
    else:
        njurado = 1
        print("\n" * 3)
        for i in range(7):
            print("Jurado n° ", njurado)
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            njurado += 1
        print("Atleta: ", nomeatleta)
        njurado = 1
        count = 0
        for i in range(7):
            print(njurado, "° Jurado : ", notas[count])
            njurado += 1
            count += 1
        print("Resultado Final:")
        print("Nome do atleta: ", nomeatleta)
        print("Melhor nota: ", max(notas))
        print("Pior nota: ", min(notas))
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print("Media: ", round(media, 2))
        natleta += 1
        print("Reiniciando em 5 segundos")
        time.sleep(5)
