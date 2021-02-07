#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@MauriSudario'
import doctest
# TODO: Atividade  1: implementar fatorial para que passe nos testes


def factorial(n):

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()


