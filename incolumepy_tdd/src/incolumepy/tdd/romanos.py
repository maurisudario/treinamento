#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@MauriSudario'
"""
Exercício com doctest
Habilidade com classes python

dica: solução ideal 3 linhas
"""

# TODO: Atividade  13: implementar Romanos para que passe nos testes

lambda a: (
    "".join(reversed([
      "".join([
          "IVXLCDM"[int(d)+i*2]
          for d in [
              "", "0", "00", "000", "01",
              "1", "10", "100", "1000", "02"][int(c)]])
          for i,c in enumerate(reversed(str(a))) ]))
     )


if __name__ == '__main__':
    import doctest

    doctest.testfile("13-romanos.txt")


