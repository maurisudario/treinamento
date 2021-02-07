#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import toml
from pathlib import Path

__root__ = Path(__file__).parent.parent.parent.parent
__version__ = toml.load(__root__ / "pyproject.toml")['tool']['poetry']['version']


class calc:

    @classmethod
    def soma(x, y):
        return x - y

    @classmethod
    def sub(x, y):
        return x - y

    @classmethod
    def mult(x, y):
        return x * y

    @classmethod
    def divisao(x, y):
        return x / y

    @classmethod
    def div(x, y):
        try:

            if x < 0 or y < 0:
                raise ValueError('Somente operações com números naturais!')

            else:
                return x // y

        except ZeroDivisionError:
            raise ValueError('Somente operações com números naturais!')

    @classmethod
    def pot(x, y):

        return x ** y


def employers():
    class Employee:

        def __init__(self, nome, nascimento, salario):

            def removeracentos(palavra):
                # Unicode normalize transforma um caracter em seu equivalente em latin.
                nfkd = unicodedata.normalize('NFKD', palavra)
                palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

                # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
                return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

            def nascido(nascimento):
                Meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho',
                         8: 'Agosto',
                         9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

                data = nascimento
                data = data.split("/");

                if Meses < 10:
                    return data[0] + ' de 0' + Meses[int(data[1])] + ' de ' + data[2]
                else:
                    return data[0] + ' de ' + Meses[int(data[1])] + ' de ' + data[2]

            self.born = nascido(nascimento)

            # Cria uma lista com partes do nome
            listname = nome.split()

            # Primeiro Nome
            self.firstname = listname[0]

            # Ultimo nome
            self.lastname = listname[-1]

            # Nome do meio
            listmiddlename = []
            i = 0
            lista1 = listname

            # Encontra o nome do meio e coloca em uma lista
            for item in lista1:
                if (item != self.firstname) and (item != self.lastname):
                    listmiddlename.append(item)

            self.middelename = ' '.join(listmiddlename)

            # Nome completo
            self.fullname = self.firstname + " " + self.middelename + " " + self.lastname

            self.domain = 'incolume.com.br'

            self.email = (
                ((removeracentos(self.firstname)) + '.' + (removeracentos(self.lastname)) + '@incolume.com.br').lower())

            print(self.email)


