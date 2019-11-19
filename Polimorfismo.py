# -*- coding: utf -8 -*-


class Perro():
    def avanzar(self):
        print("corriendo en 4 patas ")


class Perico():
    def avanzar(self):
        print("Volando")


def Mover(animal):
    animal.avanzar()


if __name__ == "__main__":
    perro=Perro()
    perico= Perico()
    perro.avanzar()
    perico.avanzar()
    print("----------------\n")
    Mover(perro)
    Mover(perico)



