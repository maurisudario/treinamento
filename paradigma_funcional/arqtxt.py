# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

import os
import pathlib


def exemplo1(valores):
    f = open(valores)
    content = f.read()
    f.close()
    return content
