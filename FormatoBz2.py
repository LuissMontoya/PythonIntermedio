# -*- coding: utf-8 -*-
import bz2

if __name__ == "__main__":
    cadena=b"Cadena Cadena Cadena Cadena Cadena"
    cadena_c= bz2.compress(cadena)
    print(cadena_c)
    print("\n")
    print(bz2.decompress(cadena_c))