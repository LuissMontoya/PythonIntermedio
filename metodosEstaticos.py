# -*- coding: utf -8 -*-


class Persona():
    def __init__(self):
        pass

    def brincar(self, mensaje):
        print("brinco")

    @classmethod
    def correr(cls):
        print("Corro")

    @staticmethod
    def nadar():
        print("Nado")


if __name__ == "__main__":
    persona1=Persona()
    persona1.nadar()
