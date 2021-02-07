# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

import unicodedata
import re

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

        #Cria uma lista com partes do nome
        listname = nome.split()

        #Primeiro Nome
        self.firstname = listname[0]

        #Ultimo nome
        self.lastname = listname[-1]

        #Nome do meio
        listmiddlename = []
        i = 0
        lista1 = listname

        # Encontra o nome do meio e coloca em uma lista
        for item in lista1:
            if (item != self.firstname) and (item != self.lastname):
                listmiddlename.append(item)

        self.middelename = ' '.join(listmiddlename)

        #Nome completo
        self.fullname = self.firstname + " " + self.middelename + " " + self.lastname

        self.domain = 'incolume.com.br'

        self.email = (((removeracentos(self.firstname)) + '.' + (removeracentos(self.lastname)) + '@incolume.com.br').lower())

        print(self.email)

