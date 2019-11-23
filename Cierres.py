# -*- coding: utf -8 -*-

# Permite tener una función dentro de otra función.

def FuncionA(x):
    def FuncionB(y):
        return x+y
    return FuncionB
    

if __name__ == "__main__":
    funcion=FuncionA(3)
    print(funcion(5))
  