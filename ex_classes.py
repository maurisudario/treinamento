# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'


def ex01():
    """ Classe Bola: Crie uma classe que modele uma bola:
    Atributos: Cor, circunferência, material
    Métodos: troca_cor e mostra_cor """

    class Ball:
        def __init__(self, cor="unknown", circf=0, material="unknown"):
            self.cor = cor
            self.circf = circf
            self.material = material

        def trocaCor(self):
            troca = input("Deseja alterar a cor atual {}? [sim/não]".format(self.cor))

            troca = troca[0].lower()

            if troca == "sim":
                nova_cor = input("\n> Insira a nova cor: ")
                self.cor = nova_cor
            else:
                print("Ok a cor permanece a mesma {}".format(self.cor))

        def mostraCor(self):
            print("\nA cor atual é: {}".format(self.cor))

    def main():
        bola01 = Ball("azul", 5, "metal")

        while True:
            bola01.mostraCor()
            bola01.trocaCor()

            continuar = input("Continuar? [s/n]")
            continuar = continuar[0].lower()
            if continuar == "n":
                break

        bola01.mostraCor()

    main()


def ex02():
    """ Classe Quadrado: Crie uma classe que modele um quadrado:
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área """


class Square:
    def __init__(self, lado="0"):
        self.lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, valor):

        if valor.isdigit():
            self.__lado = valor
        else:
            print("O valor do lado deve ser apenas numérico")

    def valorLado(self):
        print("\nO valor do lado é {} cm".format(self.__lado))

    def mudarLado(self):
        novoLado = input("\nAltere o lado de {} cm para: ".format(self.__lado))
        self.lado = novoLado

    def calcArea(self):
        print("\nA área do quadrado é {:.2f} cm²".format(
            float(self.__lado) * float(self.__lado)))

    def __str__(self):
        return "O quadrado possui {} cm de lado e {:.2f} cm² de area".format(
            self.__lado, float(self.__lado) * float(self.__lado))


def main():
    quadradoA = Square()
    lado = input("Insira o valor do lado do quadrado: ")
    quadradoA.lado = lado

    print(quadradoA)

    quadradoA.mudarLado()
    quadradoA.valorLado()
    quadradoA.calcArea()


main()


def ex03():
    """  Classe Retangulo: Crie uma classe que modele um retângulo:
    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local.
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para
    o local. Assuma rodapés com 5 cm de altura."""

    class Retangulo:
        def __init__(self, comprimento="0", largura="0"):
            self.comprimento = comprimento
            self.largura = largura

        @property
        def comprimento(self):
            return self.__comprimento

        @comprimento.setter
        def comprimento(self, valor):

            if valor.isdigit():
                self.__comprimento = valor
            else:
                print("Por favor insira apenas números.")

        @property
        def largura(self):
            return self.__largura

        @largura.setter
        def largura(self, valor):

            if valor.isdigit():
                self.__largura = valor
            else:
                print("Por favor insira apenas números")

        def mudaValor(self):
            c = input("\nComprimento: ")
            self.comprimento = c

            l = input("Largura: ")
            self.largura = l

        def mostraValor(self):
            print("\n--- Retangulo ---")
            print("Comprimento: {} m".format(self.__comprimento))
            print("Largura: {} m".format(self.__largura))
            print("-----------------")

        def calcArea(self):
            print("A área é {} m²".format(
                float(self.__comprimento) * float(self.__largura)))

        def calcPerimetro(self):
            print("O perimetro é {} m".format(
                (float(self.__comprimento) * 2) + (float(self.__largura) * 2)
            ))

    def main():
        objeto = Retangulo()
        objeto.mostraValor()

        objeto.mudaValor()
        objeto.mostraValor()

        objeto.calcArea()
        objeto.calcPerimetro()

    main()


def ex04():
    """ Classe Pessoa: Crie uma classe que modele uma pessoa:
    Atributos: nome, idade, peso e altura
    Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. """

    class Pessoa:
        def __init__(self, nome="pessoa", idade=0, peso=0, altura=0.0):
            self.nome = nome
            self.idade = idade
            self.peso = peso
            self.altura = altura

        def crescer(self, cm):
            self.altura += cm / 100
            print("{} cresceu {} cm, e agora tem {:.3f} m de altura".format(
                self.nome, cm, self.altura))

        def engordar(self, kg):
            self.peso += kg
            print("{} engordou {} kg, e agora pesa {} kg".format(
                self.nome, kg, self.peso))

        def emagrecer(self, kg):
            self.peso -= kg
            print("{} emagreceu {} kg, e agora pesa {} kg".format(
                self.nome, kg, self.peso
            ))

        def envelhecer(self, anos):
            cresc = 0

            if self.idade + anos <= 21:
                cresc = anos * 0.5

            if self.idade < 21:
                if self.idade + anos > 21:
                    cresc = ((21 - self.idade) * 0.5)

            self.idade += anos

            print("{} agora tem {} anos de idade.".format(self.nome, self.idade))
            self.crescer(cresc)

    def main():
        joao_doe = Pessoa("Joao", 12, 60, 1.68)

        print("Altura do {}: {}m ".format(joao_doe.nome, joao_doe.altura))
        C = int(input("Quanto deseja crescrer? (cm): "))
        joao_doe.crescer(C)

        print()

        print("Peso do {}: {} kg".format(joao_doe.nome, joao_doe.peso))
        E = int(input("Quanto deseja engordar? (kg): "))
        joao_doe.engordar(E)

        print()

        print("Peso do {}: {} kg".format(joao_doe.nome, joao_doe.peso))
        E = int(input("Quanto deseja emagrecer? (kg): "))
        joao - doe.emagrecer(E)

        print()

        print("A idade do {}: {} anos".format(joao_doe.nome, joao_doe.idade))
        E = int(input("Quanto deseja envelhecer? (anos): "))
        joao_doe.envelhecer(E)

    main()


def ex05():
    """ Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os
    seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterar_nome,
    depósito e saque; No construtor, o saldo é opcional, com valor default zero e os demais atributos são
    obrigatórios """

    import random
    import time

    class bankAccount:
        def __init__(self, conta, nome, saldo=0):
            self.conta = conta
            self.nome = nome
            self.saldo = saldo

        @property
        def conta(self):
            return self.__conta

        @conta.setter
        def conta(self, numero):
            valido = False

            if numero[0:4].isdigit():
                if numero[4:5] == "-":
                    if numero[5:6].isdigit():
                        valido = True
                        self.__conta = numero

            if valido == False:
                print("O numero da conta deve ser no formato [ XXXX-X ]")

        def alterarNome(self):
            verif = input("Nome atual {} \nDeseja mudar o nome? [Sim/Nao]"
                          .format(self.nome))
            verif = verif[0].upper()

            if verif == "Sim":
                novo_nome = input("Por favor insira o novo nome: ")
                self.nome = novo_nome
                print("Nome ALTERADO!")

            else:
                print("Alteração de nome CANCELADA.")

        def deposito(self):
            while True:
                try:
                    print()
                    print("Depósito na conta {}".format(self.conta))
                    valor = float(input("Qual o valor do depósito: R$ "))

                    if valor > 3000:
                        print("Não é possível realizar o depósito! "
                              "\nO valor máximo permitido é R$ 3000")
                        continue

                    self.saldo += valor
                    print("R$ {:.2f} depositado. \nNovo Saldo R$ {:.2f}".format(
                        valor, self.saldo))
                    break

                except:
                    print("Por favor insira um valor valido!")

        def saque(self):
            print()
            print("Conta {} \nSaldo disponível R$ {:.2f}".format(
                self.conta, self.saldo))
            while True:
                try:
                    valor = float(input("Qual valor deseja sacar: R$ "))

                    if valor > self.saldo:
                        print("Você não possui saldo disponível\n")
                        continue

                    self.saldo -= valor
                    print("\nSaque de R$ {:.2f} realizado! \nNovo Saldo R$ {:.2f}".format(
                        valor, self.saldo))

                    break

                except:
                    print("Por favor insira um valor valido!\n")

        def __str__(self):
            return "\n===== CONTA BANCÁRIA =====\
            \nCONTA: {} \nNOME: {} \nSALDO: R${:.2f}\
            \n==========================".format(self.conta, self.nome, self.saldo)

    def menu():
        print("======== BEM VINDO AO BANCO ========")
        print("1 - Acessar conta")
        print("2 - Criar conta")
        print("3 - Sair")
        print("====================================")
        opc = input("Selecione uma opção: ")

        return opc

    def menuConta(contas):
        print("Acessar conta ================")
        numero = input("Número da conta [ XXXX-X ]: ")

        acesso = False

        for n in contas:
            if numero == n.conta:
                acesso = True
                while True:
                    print(n)
                    print("1 - Saque")
                    print("2 - Depósito")
                    print("3 - Alterar Nome")
                    print("4 - Sair")
                    opc = input("Selecione a opção: ")

                    if opc == "1":
                        cls(50)
                        n.saque()
                    elif opc == "2":
                        cls(50)
                        n.deposito()
                    elif opc == "3":
                        cls(50)
                        n.alterarNome()
                    elif opc == "4":
                        print("Encerrando acesso...\n")
                        time.sleep(3)
                        cls(50)
                        break
                    else:
                        print("\nSelecione uma opção válida!\n")

        if acesso == False:
            print("\nConta Inválida!\n")

        return contas

    def criarConta(contas):
        print("======== Criar Conta ========")
        nome = input("NOME: ")
        numero = str(random.randrange(1000, 9999)) + "-" + \
                 str(random.randrange(1, 9))
        print("Criando conta...\n")
        time.sleep(3)
        print("CONTA CRIADA!")

        Nconta = bankAccount(numero, nome)
        contas.append(Nconta)

        print(Nconta)
        sair = input("Pressione qualquer tecla para voltar ao menu principal.")
        cls(50)

        return contas

    def cls(x):
        print("\n" * x)

    def main():
        conta01 = bankAccount("1234-5", "Joao Doe", 1250)
        contas = [conta01]

        cls(50)

        while True:
            print()
            opc = menu()

            if opc == "1":
                cls(50)
                contas = menuConta(contas)
            elif opc == "2":
                cls(50)
                contas = criarConta(contas)
            elif opc == "3":
                cls(50)
                print("Obrigado por utilizar \nEncerrando...")
                break
            else:
                print("\nSelecione uma opção válida!\n")

        for i in contas:
            print(i)

    main()


def ex06():
    """ Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
    O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
    Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. """

    import time

    class televisor:
        def __init__(self, canal="1", volume="50"):
            self.canal = canal
            self.volume = volume

        @property
        def canal(self):
            return self.__canal

        @canal.setter
        def canal(self, numero):

            if numero.isdigit():
                num = int(numero)

                if num > 0 and num <= 150:
                    self.__canal = num
                else:
                    print("Canal Inválido")

            else:
                print("O canal deve ser apenas numérico!")

        @property
        def volume(self):
            return self.__volume

        @volume.setter
        def volume(self, numero):

            if numero.isdigit():
                num = int(numero)

                if num >= 0 and num <= 100:
                    self.__volume = num
                else:
                    print("O volume deve ser entre 0 e 100")

            else:
                print("O volume deve ser apenas numérico!")

        def mudaCanal(self):
            num = input("Mudar para CANAL: ")
            self.canal = num

        def mudaVolume(self):
            num = input("Mudar para VOLUME: ")
            self.volume = num

        def __str__(self):
            return "CANAL: {} \nvolume: {}\n ".format(self.canal, self.volume)

    def main():
        tv01 = televisor()

        while True:
            print("\n" * 40)
            print(tv01)

            print("opções ---------")
            print("1 - mudar canal")
            print("2 - mudar volume")
            print("3 - desligar\n ---------------")
            selec = input("Selecionar:")

            if selec == "1":
                tv01.mudaCanal()

            elif selec == "2":
                tv01.mudaVolume()

            elif selec == "3":
                print("Desligando ...")
                break

            else:
                print("Selecione uma opção válida!")

            time.sleep(2)

    main()


def ex07():
    """ Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
    Atributos: Nome, Fome, Saúde e Idade. Métodos: Alterar Nome, Fome, Saúde e Idade;
    Retornar Nome, Fome, Saúde e Idade. Obs:
    Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
    este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
    então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada
    a qualquer momento. """

    class BichinhoVirtual:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age
            self.__hunger = 100
            self.__health = 100

        def get_name(self):
            return self.__name

        def set_name(self, new_name):
            self.__name = new_name

        def get_age(self):
            return self.__age

        def set_age(self, new_age):
            self.__age = new_age

        def get_hunger(self):
            return self.__hunger

        def set_hunger(self, new_hunger):
            self.__hunger = new_hunger

        def get_health(self):
            return self.__health

        def set_health(self, new_health):
            self.__health = new_health

        def get_humor(self):
            if self.get_hunger() >= 70 and self.get_health() >= 70:
                return "I'm happy!"

            elif self.get_hunger() >= 50 and self.get_health() >= 50:
                return "I'm not so good!"

            elif self.get_hunger() >= 30 and self.get_health() >= 30:
                return "I'm very angry!"

            else:
                return "I'm so weak that I can't answer!"

    bichinho = BichinhoVirtual("Bolinha", 2)

    print(bichinho.get_name())
    print(bichinho.get_age())
    print(bichinho.get_humor())

    bichinho.set_health(30)
    bichinho.set_hunger(70)

    print(bichinho.get_humor())


def ex08():
    """ Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estômago)
    e pelo menos os métodos comer(), ver_bucho() e digerir(). Faça um programa ou teste interativamente,
    criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
    o conteúdo do estômago a cada refeição. Experimente fazer com que um macaco coma o outro.
    É possível criar um macaco canibal? """

    class Macaco:

        def __init__(self, nome):
            self.nome = nome
            self.bucho = []

        def comer(self, objeto):
            self.bucho.append(objeto)

        def verBucho(self):
            print("Coisas no Bucho: ")
            for i in self.bucho:
                print(i)
            print("...")

        def digerir(self):
            print("Digerindo...")
            self.verBucho()
            self.bucho = []

    alimentos = ["Banana", "Maçã", "Uva"]

    def exibeMenu(macacos):
        menu = True
        print("1 - criar macaco")
        print("2 - ver macacos")
        print("3 - sair ")
        selec = input("Selecione = ")
        print()

        if selec == "1":
            nome = input("Escolha um nome para o macaco: ")
            novo_macaco = Macaco(nome)
            macacos.append(novo_macaco)

        elif selec == "2":
            macacos = menuMacacos(macacos)

        elif selec == "3":
            menu = False
        else:
            print("Selecione uma opção válida\n")

        return menu, macacos

    def menuMacacos(macacos):

        for i in range(len(macacos)):
            print("{} - {}".format(i + 1, macacos[i].nome))

        selec = input("Selecione um macaco ou pressione Enter para sair =")
        if selec.isdigit():
            selec = int(selec)
            selec = selec - 1
        else:
            return macacos

        while True:
            print("\n" * 50)

            print("\nMACACO: {}".format(macacos[selec].nome))
            print("1 - comer")
            print("2 - ver bucho")
            print("3 - digerir")
            print("4 - sair")
            op = input("Selecione = ")
            print()

            if op == "1":
                exibeAlimentos()
                n = int(input("Selecione a comida: "))
                n = n - 1
                macacos[selec].comer(alimentos[n])

            elif op == "2":
                macacos[selec].verBucho()
                c = input("Pressione qualquer tecla para continuar...")

            elif op == "3":
                macacos[selec].digerir()
                c = input("Pressione qualquer tecla para continuar...")

            elif op == "4":
                break

        return macacos

    def exibeAlimentos():
        print()
        for i in range(len(alimentos)):
            print("{} - {}".format(i + 1, alimentos[i]))

    macacos = []
    menu = True

    while menu:
        print("\n" * 50)
        menu, macacos = exibeMenu(macacos)

    print("Finalizando...")


def ex09():
    """ Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
    Possua uma classe chamada Ponto, com os atributos x e y.
    Possua uma classe chamada Retangulo, com os atributos largura e altura.
    Possua uma função para imprimir os valores da classe Ponto
    Possua uma função para encontrar o centro de um Retângulo.
    Você deve criar alguns objetos da classe Retangulo.
    Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo,
    que deve ser um objeto da classe Ponto.
    A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que
    indique os valores de x e y para o centro do objeto.
    O valor do centro do objeto deve ser mostrado na tela
    Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo. """

    class Ponto:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __str__(self):
            return "Ponto na posição X: {:.2f} e Y: {:.2f} \n".format(self.x, self.y)

    class Retangulo:
        def __init__(self, largura, altura, ponto_inicio):
            self.largura = largura
            self.altura = altura
            self.ponto_inicio = ponto_inicio

        def centro_retangulo(self):
            x = self.ponto_inicio.x + (self.largura / 2)
            y = self.ponto_inicio.y + (self.altura / 2)

            centro = Ponto(x, y)

            print("Centro:", centro)

        def __str__(self):
            return "Retângulo: largura: {} altura: {} \nInicio em x: {} e y: {} \n".format(
                self.largura, self.altura, self.ponto_inicio.x, self.ponto_inicio.y)

    def main():
        ret = criar_retangulo()
        executar = True

        while executar:
            print("\n" * 50)
            print(ret)

            print("1 - Criar Retângulo")
            print("2 - Ver centro")
            print("3 - Sair")
            op = input("Selcione uma opção = ")
            print()

            if op == "1":
                ret = criar_retangulo()

            elif op == "2":
                ret.centro_retangulo()
                cont = input("Pressione qualquer tecla para continuar...")

            elif op == "3":
                executar = False

    def criar_retangulo():
        print("------ Criar Retangulo ------")

        inicio = Ponto(0, 0)
        ret = Retangulo(5, 5, inicio)
        # Define medidas do Retangulo
        largura = float(input("Largura: "))
        altura = float(input("Altura: "))

        ret.largura = largura
        ret.altura = altura

        # Define ponto de inicio
        x = float(input("Eixo X: "))
        y = float(input("Eixo Y: "))

        inicio = Ponto(x, y)
        ret.ponto_inicio = inicio

        return ret

    main()


def ex10():
    """ Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    tipoCombustivel.
    valorLitro
    quantidadeCombustivel
    Possua no mínimo esses métodos:
    abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros
    que foi colocada no veículo
    abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
    a ser pago pelo cliente.
    alterarValor( ) – altera o valor do litro do combustível.
    alterarCombustivel( ) – altera o tipo do combustível.
    alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba. """

    import time
    class bombaCombustivel:
        tanque = {"GASOLINA": 45, "ALCOOL": 125.5, "DIESEL": 205}
        preco = {"GASOLINA": 3.24, "ALCOOL": 2.37, "DIESEL": 2.58}

        def __init__(self, tipo_combustivel="G"):
            self.tipo_combustivel = tipo_combustivel
            self.valor_litro = 0

        ### Define o tipo e preço do combústivel ###
        @property
        def tipo_combustivel(self):
            return self.__tipo_combustivel

        @tipo_combustivel.setter
        def tipo_combustivel(self, tipo):
            tipo = tipo[0].upper()

            if tipo == "G":
                print("Tipo GASOLINA Selecionado")
                self.__tipo_combustivel = "GASOLINA"
                self.valor_litro = bombaCombustivel.preco["GASOLINA"]

            elif tipo == "A" or tipo == "Á":
                print("Tipo ALCOOL Selecionado")
                self.__tipo_combustivel = "ALCOOL"
                self.valor_litro = bombaCombustivel.preco["ALCOOL"]

            elif tipo == "D":
                print("Tipo DIESEL Selecionado")
                self.__tipo_combustivel = "DIESEL"
                self.valor_litro = bombaCombustivel.preco["DIESEL"]

            else:
                print("O tipo selecionado não é válido")

        ### Inicio dos métodos ###
        def alterar_combustivel(self):
            print("\nCombustível --------------------------")
            print("G - Gasolina: R$ {}".format(bombaCombustivel.preco["GASOLINA"]))
            print("A - Álcool: R$ {}".format(bombaCombustivel.preco["ALCOOL"]))
            print("D - Diesel: R$ {}".format(bombaCombustivel.preco["DIESEL"]))
            tipo = input("Selecione o tipo desejado: ")
            self.tipo_combustivel = tipo

        def abastercer_valor(self):
            if self.valor_litro == 0:
                print("Selecione um tipo de combustível válido")

            else:
                valor = float(input("\nAbastecer Valor: R$: "))
                litros = valor / self.valor_litro

                if bombaCombustivel.qtd_disponivel(self, litros):
                    print("Abastecido {:.2f} litros de {}".format(litros, self.tipo_combustivel))

                else:
                    print("Não há combustível dispónivel")

        def abastecer_litros(self):
            if self.valor_litro == 0:
                print("Selecione um tipo de combustível válido")

            else:
                litros = float(input("\nAbastecer Litros: "))

                if bombaCombustivel.qtd_disponivel(self, litros):
                    print("{:.2f} litros de {} - Total R$ {:.2f}".format(litros,
                                                                         self.tipo_combustivel,
                                                                         (litros * self.valor_litro)))

                    dinheiro = float(input("Dinheiro: R$ "))
                    print("Troco: R$ {:.2f} \n".format(dinheiro - (litros * self.valor_litro)))

                    print("Abastecido {:.2f} litros de {}".format(litros, self.tipo_combustivel))

                else:
                    print("Não há combustível dispónivel")

        def alterar_valor(self):
            print("\n\n---------------------------------------")
            print("Alterar precos combustível")
            print("---------------------------------------")
            self.alterar_combustivel()

            novo_valor = float(input("Novo valor: R$ "))
            bombaCombustivel.preco[self.tipo_combustivel] = novo_valor

            print("{} valor alterado para R$ {}".format(
                self.tipo_combustivel, bombaCombustivel.preco[self.tipo_combustivel]))

        @staticmethod
        def alterar_qtd_combustivel():
            print("\nTanque de combustível -----------------")
            print("Gasolina: {:.2f} litros".format(bombaCombustivel.tanque["GASOLINA"]))
            print("Álcool: {:.2f} litros".format(bombaCombustivel.tanque["ALCOOL"]))
            print("Diesel: {:.2f} litros".format(bombaCombustivel.tanque["DIESEL"]))
            preencher = input("Preencher o Tanque? (s/n)")
            if preencher[0].lower() == "s":
                bombaCombustivel.tanque = {"GASOLINA": 300, "ALCOOL": 300, "DIESEL": 300}

        @staticmethod
        def qtd_disponivel(self, litros):
            # Verifica se possui combústivel do tipo selecionado dispónivel
            if litros <= bombaCombustivel.tanque[self.tipo_combustivel]:
                bombaCombustivel.tanque[self.tipo_combustivel] -= litros
                return True

            else:
                return False

    def main():
        bomba1 = bombaCombustivel()
        executar = True

        while executar:
            cls(50)
            executar = menu(bomba1)
            time.sleep(3)

    def cls(x):
        print("\n" * x)

    def menu(bomba):
        print("--------------------------------------")
        print("           POSTO IPIRANGA")
        print("--------------------------------------")
        print("1 - Escolher tipo combustível")
        print("2 - Abastecer por valor")
        print("3 - Abastecer por litros")
        print("4 - Alterar preços")
        print("5 - Preencher tanque das bombas")
        print("6 - Sair")
        print("-------------------------------------")
        print("Combustível Selecionado: {} \n".format(bomba.tipo_combustivel))
        op = input("Selecionar opção: ")

        if op == "1":
            bomba.alterar_combustivel()

        elif op == "2":
            bomba.abastercer_valor()

        elif op == "3":
            bomba.abastecer_litros()

        elif op == "4":
            bomba.alterar_valor()

        elif op == "5":
            bombaCombustivel.alterar_qtd_combustivel()

        elif op == "6":
            print("Saindo...")
            return False

        else:
            print("Selecione uma opção válida.")

        return True

    main()


def ex11():
    """ Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
    Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de
    combustível no tanque.
    O consumo é especificado no construtor e o nível de combustível inicial é 0.
    Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
    reduzindo o nível de combustível no tanque de gasolina.
    Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
    meuFusca.andar(100);            # anda 100 quilômetros.
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque."""

    class Carro:

        def __init__(self, consumo):
            self.consumo = consumo
            self.combustivel = 0

        def mover(self, km):
            consumo = self.consumo * km
            self.combustivel -= consumo

        def gasolina(self):
            return self.combustivel

        def abastecer(self, combustivel):
            self.combustivel += combustivel

    def main():
        carrinho = Carro(10)
        carrinho.abastecer(100)
        carrinho.mover(3)
        print
        carrinho.gasolina()

    import unittest

    class TestCarro(unittest.TestCase):

        def setUp(self):
            self.carro = Carro(10)

        def test_verifica_se_abasteceu_100(self):
            self.carro.abastecer(100)
            abastece = 100
            self.assertEquals(abastece, self.carro.gasolina())

        def test_move_3_resta_70_de_gasolina(self):
            self.carro.abastecer(100)
            move = 3
            self.carro.mover(3)
            self.assertEquals(70, self.carro.gasolina())

    if __name__ == '__main__':
        main()
        unittest.main()


def ex12():
    """ Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe
    contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que
    configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro
    explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo
    inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e
    imprime o saldo resultante. """

    class Investimento:
        nome = None
        numero = None
        saldo = None
        taxJur = None

        def __init__(self, nome, num, sdo, tax):
            self.nome = nome
            self.numero = num
            self.saldo = sdo
            self.taxJur = tax

        def saldo(self):
            return self.saldo

        def addJur(self):
            self.saldo += (self.taxJur / 100) * self.saldo
            return 'O novo valor é {:.2f}'.format(self.saldo)

    nome = input('Nome: ').upper()
    num = input('Conta: ')
    saldo = float(input('Digite seu valor em R$: '))
    tax = float(input('Digite a taxa de Juros: '))

    INV = Investimento(nome, num, saldo, tax)
    print(INV.addJur())
    print(INV.addJur())
    print(INV.addJur())
    print(INV.addJur())
    print(INV.addJur())


def ex13():
    """ Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string)
    e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos
    para devolver nome e salário. Escreva um pequeno programa que teste sua classe. """

    class Funcionario:
        nome = None
        salario = None

        def __init__(self, nome, salario):
            self.nome = nome
            self.salario = salario

        def nomeFunc(self):
            return self.nome

        def Salario(self):
            return self.salario

    nome = input('Nome: ').upper()
    salario = float(input('Salário: '))
    Func = Funcionario(nome, salario)
    print('O nome do(a) funcionário(a) é {} e o seu salário é de R${:.2f}'.format(Func.nomeFunc(), Func.Salario()))


def ex14():
    """ Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
    (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
     Exemplo de uso:
    harry=funcionário("Harry",25000)"""

    class Funcionario:
        nome = None
        salario = None
        tax = None

        def __init__(self, nome, salario, tax):
            self.nome = nome
            self.salario = salario
            self.tax = tax

        def nomeFunc(self):
            return self.nome

        def Salario(self):
            return self.salario

        def IncSalario(self):
            self.perc = (self.tax / 100)
            incSal = self.perc * self.salario
            novoSalario = self.salario + incSal
            self.novoSalario = novoSalario
            return self.novoSalario

    nome = input('Nome: ').upper()
    salario = float(input('Salário: '))
    tax = float(input('Taxa de aumento de salário: '))
    Func = Funcionario(nome, salario, tax)
    print('O(a) funcionário(a) {} recebe o salário de R${:.2f}'.format(Func.nomeFunc(), Func.Salario()))
    print('Após 1 ano, ele(a) receberá um salário de R${:.2f}'.format(Func.IncSalario()))


def ex15():
    """ Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário
    especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
    Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem. """

    import time
    class Tamagotchi:
        def __init__(self, nome="Tamagotchi", fome=0, saude=100, idade=1):
            self.nome = nome
            self.fome = fome
            self.saude = saude
            self.idade = idade

        # Getter and Setter Fome
        @property
        def fome(self):
            return self.__fome

        @fome.setter
        def fome(self, valor):
            if valor < 0:
                self.__fome = 0

            elif valor > 100:
                self.__fome = 100

            else:
                self.__fome = valor

        # Getter and Setter Idade
        @property
        def idade(self):
            return self.__idade

        @idade.setter
        def idade(self, valor):

            if valor > 100:
                print("Maior que 5 segundos")
                self.__idade = valor
            else:
                self.__idade = valor

        # Método Nome
        def altera_nome(self):
            self.nome = input("Qual nome deseja colocar no seu Tamagotchi? ")

        # Métodos Fome
        def reduz_fome(self, valor):
            self.fome -= valor

        def aum_fome(self, valor):
            self.fome += valor

        # Métodos Saúde
        def reduz_saude(self, valor):
            self.saude -= valor

        def aum_saude(self, valor):
            self.saude += valor

        # Metódo altera idade
        def envelhecer(self, segundos):
            # Valor pelo qual segundos são divididos definem duração de um ano de idade
            self.idade += int(segundos / 6)

        def humor(self):
            humor = (50 - (self.fome * .5)) + (self.saude * .5)

            return humor

        def __str__(self):
            return "-----Status----- \nNome:  {}  \nFome:  {} \nSaúde: {} \nIdade: {} \n \nHumor: {}".format(
                self.nome, self.fome, self.saude, self.idade, self.humor())

    def events(player, segundos):
        sair = False

        player.envelhecer(segundos)

        player.aum_fome(int(segundos / 2))

        player.reduz_saude(int(segundos))

        if player.saude < 1:
            print("\nSaúde 0")
            print("Seu tamagotchi morreu! :( \nGAME OVER!")
            sair = True

        if player.idade > 100:
            print("\nSeu tamagotchi morreu de velhice! :( \nGAME OVER!")
            sair = True

        return player, sair

    def alimentar(player):
        confirm = input("Deseja alimentar {}? (s/n)".format(player.nome))

        if confirm[0].lower() == "s":
            player.reduz_fome(30)

            print("{} foi alimentado!".format(player.nome))

        else:
            print("{} Não foi alimentado.".format(player.nome))

    def medicar(player):
        confirm = input("Deseja dar remédio a {}? (s/n)".format(player.nome))

        if confirm[0].lower() == "s":
            player.aum_saude(30)

            print("{} melhorou a saúde!".format(player.nome))
        else:
            print("{} não foi medicado.".format(player.nome))

    def desenha_tamagotchi():
        print("\n" * 30)
        print("     /\___/\  ")
        print("    /       \ ")
        print("   /   ^.^   \ ")
        print("  /    ===    \  ")
        print(" | | |     | | |   ")
        print(" \_|_|-----|_|_/  ")
        print("=================\n")

    def jogada(player):
        sair = False
        print("------------------")
        print("(1) Alimentar")
        print("(2) Dar remédio")
        print("(3) Sair")
        print("(Enter) Atualizar Status")
        selec = input("=== ")

        if selec == "1":
            alimentar(player)
        elif selec == "2":
            medicar(player)
        elif selec == "3":
            print("Saindo...")
            sair = True

        return player, sair

    def main():
        print("--------------------------")
        print("        TAMAGOTCHI")
        print("--------------------------")
        player = Tamagotchi("Tamagotchi", 90, 30)
        player.altera_nome()

        sair = False

        while not sair:
            tempo_inicio = time.time()

            desenha_tamagotchi()
            print(player)

            player, sair = jogada(player)

            tempo_fim = time.time()
            player, sair = events(player, (tempo_fim - tempo_inicio))

    main()


def ex16():
    """ Crie uma "porta escondida" no programa do programa do bichinho virtual que mostra os valores exatos
    dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu,
    for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho. """


def ex17():
    """ Crie uma Fazenda de Bichinhos instanciando vários objetos bichinhos e mantendo o controle
    deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigir
    que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
    Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos
    (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
    Para tornar o programa mais interessante, dê para cada bichinho um nível inicial aleatório de fome e tédio. """

    