#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  10: implementar circulo_area para que passe nos testes

"""
__author__ = '@MauriSudario'
from unittest import TestCase, main
import math
from src.incolumepy.tdd.geometria.circulo import circulo_area, pi
cau

class TestCirculoArea(TestCase):
    def test_area(self):
        """Testa areas quando raio >=0"""
        self.assertAlmostEqual(circulo_area(0), 0)
        self.assertAlmostEqual(circulo_area(1), pi)
        self.assertAlmostEqual(circulo_area(2.1), pi * 2.1 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, circulo_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, circulo_area, 3 + 5j)
        self.assertRaises(TypeError, circulo_area, '3')
        self.assertRaises(TypeError, circulo_area, True)
