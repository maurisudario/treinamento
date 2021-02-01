# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

from turtle import pd

import content as content
import pandas
from pprint import pprint
import pathlib
from arqtxt import exemplo1


header = ['x', 'y']

if __name__ == '__main__':
    a = pd.read_txt('valores.txt')
    print(a)













