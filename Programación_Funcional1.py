# -*- coding: utf -8 -*-
from functools import reduce
numeros = [1, 2, 3, 4]


def sumar(x, y):
    return x+y


if __name__ == "__main__":
    suma = reduce(sumar, numeros)
    print(suma)