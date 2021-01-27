# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import pytest

@pytest.fixture
def calc():
    from calc import calculadora

def test_soma(calc):
    assert calculadora('+',3, '4') == 7

def test_soma_float(calc):
    assert calculadora('+', 3, 4) == 7.0

def test_menos(calc):
    assert calculadora('-','3', 4) == -1

def test_menos_float(calc):
    assert calculadora('-',3.0, 4) == -1.0

def test_mult(calc):
    assert calculadora('*', 3, '4') == 12

def test_mult_float(calc):
    assert calculadora('*', 3, '4.0') == 12.0

def test_dividir(calc):
    assert calculadora('/', 3, '4') == .75

def test_dividir_float(calc):
    assert calculadora('/', 4, 4.0) == 1.0
    assert calculadora('/', 4, 3) == 1.3333333333333333

def test_mod(calc):
    assert calculadora('%', 4, 3) == 1
    assert calculadora('%', 12, 7) == 5

def test_pow(calc):
    assert calculadora('**', 3, 4) == 81

def test_dividir_except(calc):
    with pytest.raises(ValueError, match=r'.*y deve ser > 0.*'):
        calculadora('/', 3, 0)
        calculadora('//', 3, 0)
        calculadora('//', 3, '0')
    with pytest.raises(ValueError, match=r".* operador inválido. Use: ['+', '-', '*', '**', '//', '/', '%']"):
        calculadora('^', 3, 5)
        calculadora('+', 'a', 'b')
        calculadora('+', '0', 'b')
        calculadora('+', 'a', '0')
