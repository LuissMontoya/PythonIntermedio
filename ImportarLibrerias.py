# -*- coding: utf-8 -*-

import os
import sys


def imprimir(linea_a_imprimir):
    for contador in range(0, 10):
        print(linea_a_imprimir)


if __name__ == "__main__":
    os.system("dir")
    os.system("cls")
    imprimir(sys.argv[1])
