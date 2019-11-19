# -*- coding: utf -8 -*-


class Persona():
    def __init__(self):
        pass

    def despedir(self):
        print("Adiós")

    @classmethod
    def saludar(cls, nombre):
        print("Hola , Bienvenid@: "+nombre)


if __name__ == "__main__":
    Persona.saludar("Luis")