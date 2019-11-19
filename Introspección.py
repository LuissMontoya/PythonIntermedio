# -*- coding: utf -8 -*-


class Intro():
    atrib1=120
    def __init__(self, valor):
        self.valor = valor

    def primero(self):
        print("primer Valor")

    def segundo(self):
        print("Segundo Valor")


if __name__ == "__main__":
    intos=Intro(12)
    dir(intos)
    print(dir(intos))
    print(isinstance(intos,Intro))
    print(hasattr(intos,"Numero"))
    print(hasattr(intos,"atrib1"))