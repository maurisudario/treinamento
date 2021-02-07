# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

def ex01():
    """ Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""
    v = [x for x in range(1, 6)]

    for x in v:
        print(x, end=" ")

def ex02():
    """Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. """
    listaNumerosReais = []
    print("Informe os 10 números reais: ")
    for i in range (10):
        listaNumerosReais.append(float(input("Número " + str(i+1) + ": ")))
    listaNumerosReais.reverse()
    print(listaNumerosReais)

def ex03():
    """Faça um Programa que leia 4 notas, mostre as notas e a média na tela. """
    listaNotas = []
    media = 0
    print('Informe as 4 notas')
    for i in range(4):
        listaNotas.append(float(input('Nota ' + str(i + 1) + ':\n')))
        media += listaNotas[i]
        media = media / 4
    print(listaNotas)
    print(media)

def ex04():
    """Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
     Imprima as consoantes. """
    listaChar = []
    consoantes = 0
    print('Informe os caracters')
    for i in range(10):
        listaChar.append((input('Caracter  ' + str(i + 1) + ':\n')))
        char = listaChar[i]
        if (char not in ('a', 'e', 'i', 'o', 'u')):
            consoantes += 1
    print(consoantes)

def ex05():
    """ Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no
    vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""
    listaPar = []
    listaImpar = []
    listaNumeros = []
    numero = 0
    print('Informe os numeros:')
    for i in range(20):
        listaNumeros.append((int(input('Numero: ' + str(i + 1) + ':\n'))))
        numero = listaNumeros[i]
        print(numero)
        if (numero % 2 == 0):
            listaPar.append(numero)
        else:
            listaImpar.append(numero)
    print(listaNumeros)
    print(listaPar)
    print(listaImpar)

def ex06():
    """ Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada
    aluno, imprima o número de alunos com média maior ou igual a 7.0."""
    listaNotas = []
    notasAluno = []
    print('Notas dos Alunos')
    for i in range(10):
        media = 0
        notasAluno = []
        print('Aluno: ' + str(i + 1))
        for j in range(4):
            notasAluno.append(float(input('Nota: ' + str(j + 1) + '\n')))
            media += notasAluno[j]
            print(media)
            media = media / 4
            listaNotas.append(media)

    print(listaNotas)

def ex07():
    """Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. """
    numeros = []
    for i in range(0, 4):
        numeros.append(int(input('Informe um numero inteiro: ')))
    for i in numeros:
        soma = 0
        multiplicacao = 1
        soma += i
        multiplicacao *= i
    print(numeros)
    print('Soma dos numeros:  %d' % soma)
    print('Multiplicacao dos numeros:  %d' % multiplicacao)

def ex08():
    """ Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
     Imprima a idade e a altura na ordem inversa a ordem lida."""
    pessoas = []
    for i in range (0, 5):
        pessoa = []
        pessoa.append(input('Informe a idade da pessoa: '))
        pessoa.append(input('Informe a altura da pessoa: '))
        pessoas.append(pessoa)
        pessoas.reverse()
    for pessoa in pessoas:
        print('Idade: %s - Altura :  %s' % (pessoa[0], pessoa[1]))


def ex09():
    """ Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados
    dos elementos do vetor."""
    a = []
    for i in range (0, 10):
        a.append(int(input('Informe um numero: ')))
    somaQuadrados = 0
    for numero in a:
        somaQuadrados += (numero * numero)
    print  ('A soma dos quadrados dos numeros lidos é:  %d' % somaQuadrados)

def ex10():
    """Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
    cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. """
    vet1 = []
    vet2 = []
    vet3 = []
    print ('Informe os valores do primeiro vetor')
    for i in range (0, 10)
        vet1.append(int(input('Informe um numero: ') ))
        print ('Informe os valores do segundo vetor:  ')
    for i in range (0, 10):
        vet2.append(int(input('Informe um numero: ') ))
    for i in range (0, 10):
        vet3.append(vet1[i])
        vet3.append(vet2[i])
    print (vet3)

def ex11():
    """Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. """
    vet1 = []
    vet2 = []
    vet3 = []
    vet4 = []
    print ('Informe os valores do primeiro vetor: ')
    for i in range (0, 10):
        vet1.append(int(input('Informe um numero: ') ))
    print ('Informe os valores do segundo  vetor: ')
    for i in range (0, 10):
        vet2.append(int(input('Informe um numero: ') ))
    print ('Informe os valores do terceiro vetor: ')
    for i in range (0, 10):
        vet3.append(int(iput('Informe um numero: ') ))
    for i in range (0, 10):
        vet4.append(vet1[i])
        vet4.append(vet2[i])
        vet4.append(vet3[i])
    print(vet4)


def ex12():
    """ Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com
    mais de 13 anos possuem altura inferior à média de altura desses alunos."""

    alunos = []
    totAlunos = 5
    for i in r an ge (0, totAlunos):
        aluno = []
        aluno.append(int(input('Informe a idade do aluno: ')))
        aluno.append(float(input('Informe a altura do aluno: ')) )
        alunos.append(aluno)
    somaAltura = 0.0
    for aluno in alunos:
        somaAltura += aluno[1]
    mediaAltura = somaAltura / float(totAlunos )
    totAlunosAltos = 0
    for aluno in alunos:
        if (aluno[0] >= 13) and (aluno[1] >= mediaAltura):
            totAlunosAltos += 1
    print ('Existem  %d  alunos com mais de 13 anos acima da media de altura' %\totAlunosAltos)


def ex13():
    """Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
    Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
    e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). """

    meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
             'Outubro', 'Novembro', 'Dezembro')
    temperaturas = {}
    for mes in meses:
        temperaturas[mes] = float(input('Informe a temperatura media do mes de  %s :  ' % mes) )
        somaTemperaturas = 0.0
    for temperatura in temperaturas.values():
        somaTemperaturas += temperatura

    mediaTemperaturaAnual = somaTemperaturas / 12.0
    print ('Temperaturas acima da media anual:  %.2f' %mediaTemperaturaAnual)
    for mes in meses:
        if (temperaturas[mes] >= mediaTemperaturaAnual):
            print('%s  - %.2f ' %(mes, temperaturas[mes]))

def ex14():
    """Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
    pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
     entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". """

    print(' Programa Detetive ')
    print('Respond a as perguntas abaixo com S (sim) ou N (nao)')
    perguntas = ('Voce telefonou para a vitima? ', 'Voce esteve no local do crime? ', 'Voce mora perto da vitima? ',
                 'Voce devia para a vitima? ', 'Voce trabalhou para a vitima? ')
    respostas = []
    for pergunta in perguntas:
        respostas.append(input(pergunta).upper())

    classificacao = 0
    for resposta in respostas:
        if (resposta == 'S '):
            classificacao += 1

    if (classificacao < 2):
        print('Inocente')
    elif (classificacao == 2):
        print('Suspeito')
    elif (classificacao <= 4):
        print('Cumplice')
    else:
        print('Assassino')

def ex15():
    """Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
    entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
    Após esta entrada de dados, faça:
    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem; """

    valores = []
    valor = 0
    while (valor != -1):
        valor = int(input('Informe um valor: '))
    if (valor != -1):
        valores.append(valor)

    print ('Quantidade de valores lidos: %d' %len(valores))
    print ('valores')
    valores.reverse()
    print('valores')

    somaValores = 0
    for valor in valores:
        somaValores += valor

    media = somaValores / float(len(valores))
    print('Soma dos Valores:  %d ' %somaValores)
    print('Media dos Valores: %.2f ' %media)

    valoresAcimaDaMedia = 0
    valoresAcimaDeSete = 0
    for valor in valores:
        if (valor >= media):
            valoresAcimaDaMedia += 1
        if (valor >= 7):
            valoresAcimaDeSete += 1
    print('Valores acima da media: %d' %valoresAcimaDaMedia)


def ex16():
    """ Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base
    em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
    Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento
    de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine
    quantos vendedores receberam salários nos seguintes intervalos de valores:
    $200 - $299
    $300 - $399
    $400 - $499
    $500 - $599
    $600 - $699
    $700 - $799
    $800 - $899
    $900 - $999
    $1000 em diante"""

    salarioBase = 200
    vendedores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, 10 ):
        valorVendas = float(input('Informe o valor das vendas do vendedor: '))
        salario = valorVendas * 0.09 + salarioBase
        indice = int(salario / 100) - 1
    if (indice > 9):
        indice = 9
    elif( indice < 1):
        indice = 1
        print ('indice)
    vendedores[indice - 1] += 1
    for i in range (0, 9):
        print('%d  - %d : %d' % (i * 10 0  + 200, (i + 1) * 100 + 199, vendedores[i]))

def ex17():
    """Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs
    aninhados.
    Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do
    atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa
    que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
    o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado
    o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Resultado final:
    Atleta: Rodrigo Curvêllo
    Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    Média dos saltos: 5.9 m """

    textoSaltos = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
    nomeAtleta = (' ')
    atletas = {}
    while (nomeAtleta != ''):
        nomeAtleta = input('Atleta: ')
        if (nomeAtleta != ''):
            saltos = []
            for i in textoSaltos:
                saltos.append(float(input('%s Salto:  ' % i)))
            atletas[nomeAtleta] = saltos
    print('\nResultado Final: ')
    for (nomeAtleta, saltos) in atletas.items( ):
        print('Atleta:  %s' %nomeAtleta)
        print('Saltos:  ', saltos)
        somaSaltos = 0.0
        for salto in saltos:
            somaSaltos += salto
        print('Media dos Saltos %.2f  m' %(somaSaltos / float(len(textoSaltos) )))

def ex18():
    """ Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber
    qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa,
    que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para
    desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto,
    a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
    Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido
    for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a
    pedir outro número. Após o final da votação, o programa deverá exibir:
    O total de votos computados;
    Os númeos e respectivos votos de todos os jogadores que receberam votos;
    O percentual de votos de cada um destes jogadores;
    O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos
    e o percentual de votos dados a ele.
    Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado
    aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá
    executar o cálculo do percentual de cada jogador através de uma função.
    Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
    A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo.
    O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios
    e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes
    ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
    Enquete: Quem foi o melhor jogador?

    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 10
    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 10
    Número do jogador (0=fim): 11
    Número do jogador (0=fim): 10
    Número do jogador (0=fim): 50
    Informe um valor entre 1 e 23 ou 0 para sair!
    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 0

    Resultado da votação:

    Foram computados 8 votos.

    Jogador Votos           %
    9               4               50,0%
    10              3               37,5%
    11              1               12,5%

    O melhor jogador foi o número 8, com 4 votos, correspondendo a 50% do total de votos.  """

    votosAtletas = [0] * 23
    numeroAtleta = -1
    totalVotos = 0
    print('Enquete: Quem foi o melhor jogador?')

    while (numeroAtleta != 0):
        numeroAtleta = int(input('Numero do jogador (0=fim): '))
        if (numeroAtleta < 0) or (numeroAtleta > 23):
            print('Informe um valor entre 1 e 23 ou 0 para sair!')
        if (numeroAtleta != 0):
            votosAtletas[numeroAtleta - 1] += 1
            totalVotos += 1
    print ('Resultado da votacao: ')
    print ('Foram computados  %d  votos ' %totalVotos)
    print ('Jogador \ tVotos\ t%%')
    contador = 1
    melhorJogador = 0
    for votosAtleta in votosAtletas:
        if (votosAtleta > 0):
            print  ('%d \t%d\ t% . 2f %%' %\(contador, votosAtleta, votosAtleta / flo at (totalVotos) * 100 ))
            if (votosAtleta > votosAtletas[melhorJogador]):
                melhorJogador = contador - 1
        contador += 1
        print ('O melhor jogador foi o numero  %d , com %d votos, correspondendo a '\'%.2f  do total de votos' %\
              (melhorJogador + 1, votosAtletas[melhorJogador], votosAtletas[melhorJogador] / float(totalVotos) * 100))

def ex19():
    """Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
    quantidade de organizações:
    "Qual o melhor Sistema Operacional para uso em servidores?"

    As possíveis respostas são:

    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro
    Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
    Sistema Operacional     Votos   %
    -------------------     -----   ---
    Windows Server           1500   17%
    Unix                     3500   40%
    Linux                    3000   34%
    Netware                   500    5%
    Mac OS                    150    2%
    Outro                     150    2%
    -------------------     -----
    Total                    8800

    O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""

    sistemasOperacionais = ('Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro')
    votosSistemas = [0] * 6
    opcao = -1
    totalVotos = 0
    print('Qual o melhor Sistema Operacional para uso em servidores?')
    print('\nAs possiveis respostas sao: \n')
    i = 0
    for sistema in sistemasOperacionais:
        print('%d- %s ' % (i + 1, sistemasOperacionais[i]))
        i += 1
    while (opcao != 0):
        opcao = int(input('Sistema escolhido (0=fim): '))
        if (opcao < 0) or (opcao > 23):
            print('Informe um valor entre 1 e 6 ou 0 para  sair!')
            if (opcao != 0):
                votosSistemas[opcao - 1] += 1
                totalVotos += 1
    print('Sistema Operacional   Votos   %')
    print(' -------------------  -----   ------')
    i = 0
    maiorVoto = 0
    for sistema in sistemasOperacionais:
        print('%-21s %5d    %2.2f' %\(sistemasOperacionais[i], votosSistemas[i], votosSistemas[i] /
             float(totalVotos) * 100))
        if (votosSistemas[i] > votosSistemas[maiorVoto]):
            maiorVoto = i
        i += 1
        print(' -------------------------------- ')
        print('Total                   %3d ' %totalVotos)
        print('O sistema operacional mais votado foi o  %s ,  com   %d , correspondendo a '
              ''\'%. 2f % %  dos votos.' %\( sistemasOperacionais[maiorVoto], votosSistemas[maiorVoto],
                                             votosSistemas[maiorVoto] / float (totalVotos) * 100))

def ex20():
    """As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom
    resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação
    que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
    Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato
    laboral, chegou-se a seguinte forma de cálculo:
    a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será
    de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;
    Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos,
    impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número
    indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação.
    Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador,
    de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
    O salário de cada funcionário, juntamente com o valor do abono;
    O número total de funcionário processados;
    O valor total a ser gasto com o pagamento do abono;
    O número de funcionário que receberá o valor mínimo de 100 reais;
    O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins
    ilustrativos. Os valores podem mudar a cada execução do programa.
    Projeção de Gastos com Abono
    ============================

    Salário: 1000
    Salário: 300
    Salário: 500
    Salário: 100
    Salário: 4500
    Salário: 0

    Salário    - Abono
    R$ 1000.00 - R$  200.00
    R$  300.00 - R$  100.00
    R$  500.00 - R$  100.00
    R$  100.00 - R$  100.00
    R$ 4500.00 - R$  900.00

    Foram processados 5 colaboradores
    Total gasto com abonos: R$ 1400.00
    Valor mínimo pago a 3 colaboradores
    Maior valor de abono pago: R$ 900.00 """

    salarios = []
    salarioFuncionario = -1
    print('Projecao de Gastos com Abono')
    print('============================ \n')
    while (salarioFuncionario != 0):
        salarioFuncionario = float(input('Salario: '))
        if (salarioFuncionario < 0):
            print('Informe um valor maior que 0 ou 0 para sair!')
    continue
        if (salarioFuncionario != 0):
        salarios.append(salarioFuncionario)

    print(' Salario \ tAbono')
    totalAbono = 0.0
    totalPiso = 0
    for salario in salarios:
        abono = salario * 0.2
        if (abono < 100):
        abono = 100.0
        totalPiso += 1
        totalAbono += abono
        if ('maiorAbono' not in vars() ) or (abono > maiorAbono):
            maiorAbono = abono
        print('R$  %.2 f\tR$%.2f' %(salario, abono))
    print('Foram processados  %d  votos' %len(salarios))
    print('Total gasto com abonos: %.2f ' %totalAbono)
    print('Valor minimo pago a  %d  colaboradores' %totalPiso)
    print('Maior valor de abono pago:  %.2f' %maiorAbono)

def ex21():
    """ Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos:
    FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos
    quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
    O modelo do carro mais econômico;
    Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma
    distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
    Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
    Os dados são fictícios e podem mudar a cada execução do programa.
    Comparativo de Consumo de Combustível

    Veículo 1
    Nome: fusca
    Km por litro: 7
    Veículo 2
    Nome: gol
    Km por litro: 10
    Veículo 3
    Nome: uno
    Km por litro: 12.5
    Veículo 4
    Nome: Vectra
    Km por litro: 9
    Veículo 5
    Nome: Peugeout
    Km por litro: 14.5

    Relatório Final
    1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
    2 - gol             -   10.0 -  100.0 litros - R$ 225.00
    3 - uno             -   12.5 -   80.0 litros - R$ 180.00
    4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
    5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
    O menor consumo é do peugeout. """

    print('Comparativo de Consumo de Combustivel')
    veiculos = []
    consumo = []
    preco = 2.25
    for i in range (1, 6):
        veiculos.append(input('Veiculo  %d:  ' % i) )
        consumo.append(float(input('Km por litro: ') ))
    print('Relatorio Final')
    for i in range (0, 5):
        custo = 1000 / consumo[i]
        gasto = custo * preco
        print('%d  -  %s - %.2f  -  %.f  litros  - R$ %.2f ' %\(i + 1, veiculos[i], consumo[i], custo, gasto) if ('menorConsumo' not in va rs ()) or
             (consumo[i] > consumo[menorConsumo]): menorConsumo = i)
        print('O menor consumo é do  %s' % veiculos[menorConsumo])

def ex22():
    """ Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
    com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é
    testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles,
    para verificar o que se pode aproveitar deles.
    Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber
    um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
    necessita da esfera;
    necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação
    igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
    Quantidade de mouses: 100

    Situação                        Quantidade              Percentual
    1- necessita da esfera                  40                     40%
    2- necessita de limpeza                 30                     30%
    3- necessita troca do cabo ou conector  15                     15%
    4- quebrado ou inutilizado              15                     15% """

    idMouse = -1
    defeitos = ('1   -  Necessita de Esfera', '2  -  Necessita de limpeza', '3  - Necessita troca de cabo ou conector',
                '4  - Quebrado ou inutilizado')
    totalDefeitos = [0] * 4
    totalMouses = 0
    for i in defeitos:
        print('%s' % i)
    while (id Mouse != 0):
        idMouse = int(input('Identificador do Mouse: '))
        if (idMouse != 0):
            defeito = int(input('Codigo do defeito: '))
            totalDefeitos[defeito - 1] += 1
            totalMouses += 1
    print('Quantidade de mouses:  %d  ' %totalMouses)
    print('Situacao \tQuantidade \tPercentual')
    for i in range (0, len(defeitos)):
        print('%s\t%d\t%.2 f' %\(defeitos[i], totalDefeitos[i], totalDefeitos[i] / float(totalMouses) * 100))

def ex23():
    """ A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no
    seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa
    saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
    Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125

    Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um
    programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
    ACME Inc.               Uso do espaço em disco pelos usuários
    ------------------------------------------------------------------------
    Nr.  Usuário        Espaço utilizado     % do uso

    1    alexandre       434,99 MB             16,85%
    2    anderson       1187,99 MB             46,02%
    3    antonio         117,73 MB              4,56%
    4    carlos           87,03 MB              3,37%
    5    cesar             0,94 MB              0,04%
    6    rosemary        752,88 MB             29,16%

    Espaço total ocupado: 2581,57 MB
    Espaço médio ocupado: 430,26 MB
    O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
    de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
    deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do
    percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal."""

    arquivoEntrada = open('23_entrada.txt','r ')
    # Coloca todas as linhas em memoria
    linhas = arquivoEntrada.readlines()
    # Fecha o arquivo  arquivoEntrada.close()
    usuarios = []
    espacosUtilizados = []
    espacoTotal = 0.0
    for  linha  in  linhas:
        campos = linha.split()
        usuario  =  campos [0]
        espacoUtilizado  = int(campos [1])
        usuarios.append(usuario)
        espacosUtilizados.append(espacoUtilizado)
        espacoTotal +=  espacoUtilizado
    # Abre o arquivo para escrita
    arquivoSaida = open ('23_saida.txt' , 'w')
    arquivoSaida.write('ACME Inc.               Uso do espaco em disco pelos usuarios\n')
    arquivoSaida.write('------------------------------------------------------------------------')
    arquivoSaida.write('\nNr.  Usuario        Espaco utilizado     %% do  uso ')
    for i in range (0, len(usuarios)):
        espacoMB = espacosUtilizados[i] / (1024.0 * 1024.0)
        percentualUso = espacosUtilizados[i] / espacoTotal
        arquivoSaida.write('\n%d - %s  -  %.2f  MB  - %.2f %% ' %
                           (i + 1, usuarios[i], espacoMB, percentualUso * 100.0))
        arquivoSaida.write('\nEspaco total ocupado:  %.2f  MB' % (espacoTotal / (10 24.0 * 1 02 4. 0)))
        arquivoSaida.write('\nEspaco medio ocupado:  %.2f  MB' % (espacoTotal / l en (usuarios) /
                           (1024.0 * 1024.0)))

        # Fecha o arquivo
    arquivoSaida.close()

def ex24():
    """ Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados
    em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6)
    e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados."""

    import random
    dado = [0] * 6
    for i in range (0, 100):
        lancamento = random.randint(0, 5)
        dado[lancamento] += 1
    for i in range (0, 6):
        print('%d - %d' %(i + 1, dado[i]))
