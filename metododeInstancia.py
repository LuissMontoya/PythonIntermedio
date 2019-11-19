# -*- coding: utf-8 -*-
class Persona():
    edad=19
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def nadar(self):
        print("Estoy nadando")


if __name__ == "__main__":
    persona1 = Persona("Jose", "Mexicano")
    print(Persona.edad)
    persona1.nadar()
