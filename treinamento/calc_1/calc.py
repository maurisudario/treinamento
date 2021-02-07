# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'


def calculadora(op, num1:int, num2:int):
    """Retorna o resultado da operação.

    >>> calculadora('+',3, 4)
    7

    Operações com int e float retornam float
    >>> calculadora('+',3, 4.0)
    7.0
    >>> calculadora('-',3, 4)
    -1
    >>> calculadora('-',3.0, 4)
    -1.0
    >>> calculadora('-',4, 3)
    1
    >>> calculadora('*',3, 4)
    12
    >>> calculadora('*',3, 4.0)
    12.0
    >>> calculadora('/',3, 4)
    0.75
    >>> calculadora('/',4, 3)
    1.3333333333333333
    >>> calculadora('//',4, 3)
    1

    Resto inteiro de uma divisão (mod)
    >>> calculadora('%', 4, 3)
    1
    >>> calculadora('%', 12, 7)
    5

    potência
    >>> calculadora('**',3, 4)
    81

    Exceções
    >>> calculadora('/', 3, 0)
    Traceback (most recent call last):
    ...
    ValueError: y deve ser > 0
    >>> calculadora('//', 3, 0)
    Traceback (most recent call last):
    ...
    ValueError: y deve ser > 0
    >>> calculadora('^', 3, 5)
    Traceback (most recent call last):
    ...
    ValueError: operador inválido. Use: ['+', '-', '*', '**', '//', '/', '%']
    >>> calculadora('+', 'a', 'b')
    Traceback (most recent call last):
    ...
    ValueError: x e y devem ser numéricos
    """

    l = ['+', '-', '*', '**', '//', '/', '%']
    if op not in l:
        raise ValueError("operador inválido. Use: ['+', '-', '*', '**', '//', '/', '%']")

    if op in ['/', '//'] and num2 == 0:
        raise ValueError("y deve ser > 0")
    try:
        int(num1)
        int(num2)
    except ValueError:
        raise ValueError("x e y devem ser numéricos")

    num1, num2 = str(num1), str(num2)
    result = eval("%s%s%s" %(num1, op, num2))
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

