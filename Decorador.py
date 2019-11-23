# -*- coding: utf -8 -*-

def FuncionD(Funcion):
    def PrimerD(*arg,**kkwars):
        print("Primer decorador")
    return PrimerD


@FuncionD    
def Funcion():
    print("Mi primer decorador")

if __name__ == "__main__":
    Funcion()

    